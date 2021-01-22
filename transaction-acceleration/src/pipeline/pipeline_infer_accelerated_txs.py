from tqdm import tqdm
from utils import BTC_Com, FileManager, LoggerFactory, ThreadPool

logger = LoggerFactory.get_logger('logger_application')


class CheckAcceleratedTxs:
    def __init__(self, filename='txids-acceleration.json', n_processes=50):
        self.filename = filename
        self.n_processes = n_processes
        self.btc_api = BTC_Com()
        self.txids = list()
        self.txs_acceleration = None
        logger.info(
            f"Parameters(n_processes={n_processes})")

    def execute(self):
        logger.info('START: AccelerationPrice')
        self.__load_txids()
        self.__crawl_txs_data_from_btc_com()
        self.__persist()
        logger.info('DONE: AccelerationPrice')

    def __crawl_txs_data_from_btc_com(self):
        logger.info(
            'START: Crawl transactions from BTC.com acceleration service')
        pool = ThreadPool(num_threads=self.n_processes, save_results=True)
        pbar = tqdm(desc="Crawling txs. prices",
                    total=len(self.txids), ascii=True)
        for txid in self.txids:
            pbar.update(1)
            pool.add_task(self._crawl_tx_price, txid)
        pool.wait_completion()
        pbar.close()
        self.txs_acceleration = list(pool.get_results())
        logger.info(
            'DONE: Crawl transactions from BTC.com acceleration service')

    def _crawl_tx_price(self, txid):
        tx_price = {'txid': txid, 'info': None}
        try:
            tx_price['info'] = self.btc_api.get_info(txid=txid)
        except:
            logger.error("Error on _crawl_tx_price", exc_info=True)
        return tx_price

    def __load_txids(self):
        self.txids = FileManager.load_json(
            filename=self.filename, compression=False)[0]

    def __persist(self):
        FileManager.dump_raw_json(
            data=self.txs_acceleration, filename=f"tx-acceleration-raw-data.json.gz")
