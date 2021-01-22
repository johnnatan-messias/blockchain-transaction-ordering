import numpy as np
from utils import FileManager, LoggerFactory

logger = LoggerFactory.get_logger('logger_application')


class SelectTxs:
    def __init__(self, mempool_data):
        self.datetime = mempool_data['datetime']
        self.mempool_df = mempool_data['mempool_df']
        self.mempool_info = mempool_data['mempool_info']
        self.selected_txs = None
        logger.info(
            f"Parameters(is_mempool_congestion={mempool_data['status']})")

    def execute(self):
        logger.info('START: SelectTx')
        self.__pre_process_mempool()
        self.__select_best_txs()
        self.__persist()
        logger.info('DONE: SelectTx')

    def __pre_process_mempool(self):
        # Removing transactions that depend on others (CPFP-txs).
        self.mempool_df.query('ancestorcount == 1', inplace=True)
        # Creating the fee-per-byte (feerate) attribute.
        self.mempool_df['feerate'] = (
            (1e8 * self.mempool_df['fee']) / self.mempool_df['size']).apply(np.ceil).astype(int)
        # We consider only transactions that offer at least the minimum suggested fee (1 sat per byte)
        self.mempool_df.query('feerate >= 1', inplace=True)
        # TXID is now the dataframe index
        # self.mempool_df.set_index('txid', inplace=True)

    def __select_best_txs(self):
        logger.info('START: Select best transactions for acceleration')
        self.__get_acceleration_fee_estimation()
        logger.info('DONE: Select best transactions for acceleration')

    def __persist(self):
        FileManager.dump_dataframe(
            dataframe=self.selected_txs, filename=f"selected_txs_{self.datetime}.tsv.gz")

    def __get_acceleration_fee_estimation(self):
        # less fee; less size -> less acceleration fee
        self.selected_txs = self.mempool_df.query(
            'feerate <= 2').sort_values('size')[
                ['txid', 'feerate', 'fee', 'size', 'time', 'height']
        ]

        logger.info(
            f"The best 5 transactions cadidates are: {self.selected_txs.head(5).txid.tolist()}")
