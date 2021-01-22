import argparse

from pipeline import PipelineFactory
from utils import ApplicationPaths, LoggerFactory

logger = LoggerFactory.get_logger("logger_application")


def run_transaction_acceleration_price(mempool_data):
    PipelineFactory.acceleration_price(mempool_data=mempool_data)


def run_transaction_selection_for_acceleration_experiment(mempool_data):
    PipelineFactory.select_txs(mempool_data=mempool_data)


def run_is_transactions_accelerated(filename):
    PipelineFactory.check_accelerated_txs(filename=filename)


def main(args):
    mempool_data = PipelineFactory.mempool_transactions(mempool_congestion=16)
    is_mempool_congested = mempool_data['status']
    logger.info(f"Is Mempool congested? {is_mempool_congested}")

    if is_mempool_congested:
        run_transaction_selection_for_acceleration_experiment(
            mempool_data=mempool_data)
        run_transaction_acceleration_price(mempool_data=mempool_data)

    else:
        logger.info(
            "As the mempool is not congested the execution was aborted!")

    run_is_transactions_accelerated(filename=args.filename)


if __name__ == "__main__":
    ApplicationPaths.makedirs()

    parser = argparse.ArgumentParser(
        description="Bitcoin transaction acceleration analysis")

    parser.add_argument('--routine', type=str, help='It defines the routine execution',
                        choices=['select_transactions', 'compare_price', 'is_txs_accelerated'])

    args = parser.parse_args()

    main(args)
