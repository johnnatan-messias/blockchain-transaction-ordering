from utils import LoggerFactory

from .pipeline_acceleration_price import AccelerationPrice
from .pipeline_crawl_txs import CrawlTxs
from .pipeline_infer_accelerated_txs import CheckAcceleratedTxs
from .pipeline_select_txs import SelectTxs

logger = LoggerFactory.get_logger("logger_application")


class PipelineFactory:

    @staticmethod
    def mempool_transactions(mempool_congestion=16):
        crawler = CrawlTxs(mempool_congestion=mempool_congestion)
        response = crawler.execute()
        return response

    @staticmethod
    def acceleration_price(mempool_data):
        acceleration = AccelerationPrice(mempool_data)
        acceleration.execute()

    @staticmethod
    def select_txs(mempool_data):
        select_txs = SelectTxs(mempool_data)
        select_txs.execute()

    @staticmethod
    def check_accelerated_txs(filename_in, filename_out):
        accelerated_txs = CheckAcceleratedTxs(filename_in=filename_in, filename_out=filename_out)
        accelerated_txs.execute()
