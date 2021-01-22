from tqdm import tqdm
from utils import BlockchainRPC, LoggerFactory, ThreadPool

logger = LoggerFactory.get_logger("logger_blockchain")


class Blockchain:
    def __init__(self, n_process=8, auth=('john', 'bitcoinjohnmejohnmpi')):
        self.n_process = n_process
        self.auth = auth
        self.__connect()

    def __connect(self):
        self.rpc = BlockchainRPC(self.auth)

    def get_block(self, block_hash, verbosity=2):
        logger.info(f"Get block hash={block_hash} and verbosity={verbosity}")
        block = dict()
        try:
            block = self.rpc.getblock(
                header_hash=block_hash, verbosity=verbosity)
            block = block['result']
        except:
            logger.error("Error on get_block", exc_info=True)
        return block

    def get_block_by_height(self, height, verbosity=2):
        logger.info(f"Get block height={height} and verbosity={verbosity}")
        block = dict()
        try:
            block_hash = self.rpc.getblockhash(height=height)['result']
            block = self.rpc.getblock(
                header_hash=block_hash, verbosity=verbosity)
        except:
            logger.error("Error on get_block_by_height", exc_info=True)
        return block

    def get_block_header_by_height(self, height, in_json=True):
        logger.info(f"Get block height={height} and in_json={in_json}")
        block = dict()
        try:
            block_hash = self.rpc.getblockhash(height=height)['result']
            block = self.rpc.getblockheader(
                header_hash=block_hash, in_json=in_json)
        except:
            logger.error("Error on get_block_by_height", exc_info=True)
        return block

    def get_block_header(self, block_hash, in_json=True):
        logger.info(f"Get block block_hash={block_hash} and in_json={in_json}")
        block = dict()
        try:
            block = self.rpc.getblockheader(
                header_hash=block_hash, in_json=in_json)
        except:
            logger.error("Error on get_block_header", exc_info=True)
        return block

    def get_blocks(self, block_hashes, verbosity=1):
        logger.info(
            f"Get blocks {len(block_hashes)} hashes and verbosity={verbosity}")
        logger.info(f"Using {self.n_process} processors")
        pool = ThreadPool(num_threads=self.n_process, save_results=True)
        for block_hash in tqdm(block_hashes):
            pool.add_task(self.get_block, block_hash)
        pool.wait_completion()
        results = pool.get_results()
        pool.terminate()
        return results

    def get_blocks_by_height(self, block_heights, verbosity=2):
        results = list()
        logger.info(
            f"Get blocks {len(block_heights)} heights and verbosity={verbosity}")
        logger.info(f"Using {self.n_process} processors")
        pool = ThreadPool(num_threads=self.n_process, save_results=True)
        pbar = tqdm(desc='Gathering blocks', ascii=True,
                    total=len(block_heights))
        for block_height in block_heights:
            pbar.update(1)
            pool.add_task(self.get_block_by_height, block_height, verbosity)
        pbar.close()
        logger.info('START: Removing invalid response')
        pbar = tqdm(desc='Filtering data', ascii=True)
        for block in pool.get_results():
            pbar.update(1)
            if 'result' in block:
                results.append(block)
        pbar.close()
        logger.info('DONE: Removing invalid response')
        pool.terminate()
        return results

    def get_transaction(self, txid, verbosity=True):
        logger.info(f"Get transaction txid={txid} and verbosity={verbosity}")
        tx = dict()
        try:
            tx = self.rpc.getrawtransaction(txid=txid, verbosity=verbosity)
        except:
            logger.error("Error on get_transaction", exc_info=True)
        return tx

    def get_transactions(self, txids, verbosity=True):
        results = list()
        logger.info(f"Get txs {len(txids)} txs and verbosity={verbosity}")
        logger.info(f"Using {self.n_process} processors")
        pool = ThreadPool(num_threads=self.n_process, save_results=True)
        pbar = tqdm(desc='Gathering transactions',
                    total=len(txids), ascii=True)
        for txid in txids:
            pbar.update(1)
            pool.add_task(self.get_transaction, txid)
        pool.wait_completion()
        pbar.close()
        logger.info('START: Removing invalid response')
        pbar = tqdm(desc='Filtering data', ascii=True)
        for tx in pool.get_results():
            pbar.update(1)
            if 'result' in tx:
                results.append(tx)
        pbar.close()
        logger.info('DONE: Removing invalid response')
        pool.terminate()
        return results

    def get_raw_mempool(self, verbosity=True):
        logger.info(f"START: Get raw mempool verbosity={verbosity}")
        mempool = dict()
        try:
            mempool = self.rpc.getrawmempool(verbose=True)['result']
        except:
            logger.error("Error on get_raw_mempool", exc_info=True)
        logger.info(f"DONE: Get raw mempool verbosity={verbosity}")
        return mempool

    def get_mempool_info(self):
        logger.info("START: Get mempool info")
        mempool_info = dict()
        try:
            mempool_info = self.rpc.getmempoolinfo()['result']
        except:
            logger.error("Error on get_mempool_info", exc_info=True)
        logger.info("DONE: Get mempool info")
        return mempool_info
