import argparse

from pipeline import PipelineFactory
from utils import ApplicationPaths, LoggerFactory

logger = LoggerFactory.get_logger("logger_application")


def run_transaction_acceleration_price(mempool_data):
    PipelineFactory.acceleration_price(mempool_data=mempool_data)


def run_transaction_selection_for_acceleration_experiment(mempool_data):
    PipelineFactory.select_txs(mempool_data=mempool_data)


def run_is_transactions_accelerated(filename_in, filename_out):
    PipelineFactory.check_accelerated_txs(filename_in=filename_in, filename_out=filename_out)


def main(args):
    if args.routine == 'is_txs_accelerated':
        run_is_transactions_accelerated(filename_in=args.filename_in, filename_out=args.filename_out)

    elif args.routine == 'select_transactions':
        mempool_data = PipelineFactory.mempool_transactions(
            mempool_congestion=16)
        is_mempool_congested = mempool_data['status']
        logger.info(f"Is Mempool congested? {is_mempool_congested}")

        if is_mempool_congested:
            run_transaction_selection_for_acceleration_experiment(
                mempool_data=mempool_data)
            run_transaction_acceleration_price(mempool_data=mempool_data)

        else:
            logger.info(
                "As the mempool is not congested the execution was aborted!")


if __name__ == "__main__":
    ApplicationPaths.makedirs()

    parser = argparse.ArgumentParser(
        description="Bitcoin transaction acceleration analysis")

    parser.add_argument('--routine', type=str, help='It defines the routine execution',
                        choices=['select_transactions',
                                 'compare_price', 'is_txs_accelerated'],
                        required=True)
    parser.add_argument('--filename_in', type=str,
                        help='Indicate the file that contains the txids you wish to test for acceleration')
    parser.add_argument('--filename_out', type=str,
                        help='Indicate the filename to persist the results')

    args = parser.parse_args()

    main(args)
