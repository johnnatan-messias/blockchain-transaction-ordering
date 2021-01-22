import pandas as pd
from tqdm import tqdm
from utils import BTC_Com, FileManager, LoggerFactory, ThreadPool

logger = LoggerFactory.get_logger('logger_application')


class AccelerationPrice:
    def __init__(self, mempool_data, n_processes=50):
        self.n_processes = n_processes
        self.btc_api = BTC_Com()
        self.datetime = mempool_data['datetime']
        self.mempool_df = mempool_data['mempool_df']
        self.mempool_info = mempool_data['mempool_info']
        self.txs_acceleration_prices = None
        logger.info(
            f"Parameters(n_processes={n_processes}; is_mempool_congestion={mempool_data['status']})")

    def execute(self):
        logger.info('START: AccelerationPrice')
        self.__crawl_txs_prices()
        self.__persist()
        logger.info('DONE: AccelerationPrice')

    def __crawl_txs_prices(self):
        logger.info('START: Crawl transactions prices')
        pool = ThreadPool(num_threads=self.n_processes, save_results=True)
        pbar = tqdm(desc="Crawling txs. prices",
                    total=self.mempool_df.shape[0], ascii=True)
        for txid in self.mempool_df.txid.unique():
            pbar.update(1)
            pool.add_task(self._crawl_tx_price, txid)
        pool.wait_completion()
        pbar.close()
        results = pool.get_results()
        self.txs_acceleration_prices = self.process_results_to_dataframe(
            results)
        logger.info('DONE: Crawl transactions prices')

    def _crawl_tx_price(self, txid):
        tx_price = {'txid': txid, 'info': None}
        try:
            tx_price['info'] = self.btc_api.get_info(txid=txid)
        except:
            logger.error("Error on _crawl_tx_price", exc_info=True)
        return tx_price

    def process_results_to_dataframe(self, results):
        data = list()
        for result in results:
            if 'info' in result and 'data' in result['info']:
                info = {'txid': result['txid']}
                info['size'] = result['info']['data']['size']
                info['children_total_size'] = result['info']['data']['children_total_size']
                info['flatten_tree'] = ','.join(
                    result['info']['data']['flatten_tree'])
                info['price_usd'] = result['info']['data']['price_usd']/100
                info['discount_usd'] = result['info']['data']['discount_usd']/100
                info['price_cny'] = result['info']['data']['price_cny']/100
                info['discount_cny'] = result['info']['data']['discount_cny']/100
                data.append(info)
        return pd.DataFrame(data)

    def __persist(self):
        FileManager.dump_dataframe(
            dataframe=self.txs_acceleration_prices, filename=f"tx_acceleration_prices_{self.datetime}.tsv.gz")
