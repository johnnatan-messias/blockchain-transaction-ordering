from datetime import datetime

import pandas as pd
from blockchain import Blockchain
from utils import Common, FileManager, LoggerFactory

logger = LoggerFactory.get_logger('logger_application')


class CrawlTxs:
    def __init__(self, mempool_congestion=16):
        self.mempool_congestion = 1e6 * mempool_congestion
        self.datetime = str(datetime.utcnow())
        self.blockchain = Blockchain()
        self.mempool_df = None
        self.mempool_info = None
        self.txs_acceleration_prices = None
        logger.info(
            f"Parameters(mempool_congestion={mempool_congestion})")

    def execute(self):
        logger.info('START: CrawlTxs')
        self.__get_mempool_info()
        logger.info(
            f"Mempool is {'' if self.__is_mempool_congested() else 'not'} congested")
        if self.__is_mempool_congested():
            self.__mempool_to_dataframe()
            self.__persist()
        logger.info('DONE: CrawlTxs')
        return {'mempool_df': self.mempool_df, 'mempool_info': self.mempool_info,
                'datetime': self.datetime, 'status': self.__is_mempool_congested()}

    def __get_mempool_info(self):
        self.mempool_info = self.blockchain.get_mempool_info()
        logger.info(
            f"There are {Common.to_english_number_format(self.mempool_info['size'])} transactions \
                using {Common.to_english_number_format(self.mempool_info['bytes'])} virtual bytes of the mempool")

    def __mempool_to_dataframe(self):
        mempool = self.blockchain.get_raw_mempool()
        self.mempool_df = pd.DataFrame.from_dict(mempool, orient='index')
        self.mempool_df.index.rename('txid', inplace=True)
        self.mempool_df['time'] = pd.to_datetime(
            self.mempool_df['time'], unit='s')
        self.mempool_df.reset_index(inplace=True)
        logger.info(f"MemPool Size={self.mempool_df.shape[0]}")

    def __is_mempool_congested(self):
        return self.mempool_info['bytes'] >= self.mempool_congestion

    def __persist(self):
        FileManager.dump_dataframe(
            dataframe=self.mempool_df, filename=f"mempool_df_{self.datetime}.tsv.gz")
        FileManager.dump_raw_json(
            data=self.mempool_info, filename=f"mempool_info_{self.datetime}.json", compression=False)
