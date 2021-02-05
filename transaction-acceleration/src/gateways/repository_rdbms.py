import json

import psycopg2
from psycopg2.extras import DictCursor, RealDictCursor, execute_batch

from utils import LoggerFactory
from utils.application_paths import ApplicationPaths
from utils.singleton import Singleton

logger = LoggerFactory.get_logger("logger_application")

table_blockchain_block = 'blockchain_block'
table_blockchain_transaction = 'blockchain_transaction'

blockchain_block_keys = {'block_height': '%s::INT',
                         'block_hash': '%s::TEXT', 'block_json': '%s::JSONB'}
blockchain_transaction_keys = {
    'txid': '%s::TEXT', 'block_height': '%s::INT', 'block_hash': '%s::TEXT', 'tx_json': '%s::JSONB', 'tx_position': '%s::INT'}


@Singleton
class RepositoryRDBMS:
    __conn = None

    def __init__(self):
        logger.info(">>> Connecting to the database")
        json_str = open(ApplicationPaths.config() + "db_auth.json").read()
        db_auth = json.loads(json_str)
        self.__conn = self.__connect_database(host=db_auth['host'],
                                              port=db_auth['port'],
                                              user=db_auth['user'],
                                              password=db_auth['password'], db=db_auth['db'])
        logger.info(
            f">>> Database {db_auth['db']} connected on server {db_auth['host']}:{db_auth['port']})")

    def __connect_database(self, host, port, user, password, db):
        conn_string = f"host={host} port={port} dbname={db} user={user} password={password}"
        conn = psycopg2.connect(conn_string)
        return conn

    def get_block_heights(self):
        sql = f"SELECT DISTINCT block_height FROM {table_blockchain_block};"
        data = self.__select(sql=sql, cursor_factory=None)
        return set([elem[0] for elem in data])

    def get_block_by_height(self, block_height):
        sql = f"SELECT block_json FROM {table_blockchain_block} WHERE block_height = {block_height};"
        data = self.__select(sql=sql)
        return data

    def get_block_by_hash(self, block_height):
        sql = f"SELECT block_json FROM {table_blockchain_block} WHERE block_hash = {block_hash};"
        data = self.__select(sql=sql)
        return data

    def get_block_timestamp(self, min_height, max_height):
        sql = f"SELECT block_height, block_json->'nTx' as ntx, block_json->'time' as timestamp FROM {table_blockchain_block} WHERE block_height >= {min_height} and block_height <= {max_height} ORDER BY block_height;"
        data = self.__select(sql=sql)
        return data

    def get_number_of_transactions_per_block(self):
        sql = f"SELECT block_height, block_json#>>'{nTx}' AS block_ntx FROM {table_blockchain_block};"
        data = self.__select(sql=sql)
        return data

    def get_amount_of_transactions(self):
        sql = f"SELECT block.block_height, block.ntx, transaction.ntx FROM (SELECT block.block_height, block.block_json#>>'{nTx}' AS ntx FROM {table_blockchain_block} block) JOIN (SELECT transaction.block_height, count(*) AS ntx FROM {table_blockchain_transaction} transaction GROUP BY block_height) ON block.block_height = transaction.block_height) WHERE block.ntx <> transaction.ntx;"
        data = self.__select(sql=sql)
        return data

    def get_transaction(self, txid):
        # TODO fix me
        response = list()
        sql = f"SELECT block_height, block_hash, tx_json FROM {table_blockchain_transaction} WHERE txid = '{txid}';"
        data = self.__select(sql=sql)
        if len(data) != 0:
            response = data[0]
        return response

    def get_all_transactions_from_database(self, min_height, max_height):
        response = list()
        sql = f"SELECT txid, block_height, tx_position, tx_json FROM {table_blockchain_transaction} WHERE block_height >= {min_height} AND block_height <= {max_height} ORDER BY block_height;"
        data = self.__select(sql=sql)
        if len(data) != 0:
            response = data
        return response

    def get_coinbase_transactions_from_database(self, min_height, max_height):
        response = list()
        sql = f"SELECT txid, block_height, tx_json FROM {table_blockchain_transaction} WHERE tx_position = 0 AND block_height >= {min_height} AND block_height <= {max_height} ORDER BY block_height;"
        data = self.__select(sql=sql)
        if len(data) != 0:
            response = data
        return response

    def get_transactions_by_block(self, block_height):
        sql = f"SELECT txid, block_height, tx_position, tx_json FROM {table_blockchain_transaction} WHERE block_height={block_height};"
        data = self.__select(sql=sql)
        return data

    def __parser_transaction(self, txs, block_height, block_hash):
        tx_data = list()
        #tx_ids = list(map(lambda tx: tx['txid'], txs))
        #tx_positions = dict(zip(tx_ids, range(len(tx_ids))))
        tx_pos = 0
        for tx in txs:
            tx_dict = dict()
            tx_dict['txid'] = tx['txid']
            tx_dict['block_height'] = block_height
            tx_dict['block_hash'] = block_hash
            tx_dict['tx_json'] = json.dumps(tx)
            #tx_dict['tx_position'] = tx_positions[tx['txid']]
            tx_dict['tx_position'] = tx_pos
            tx_pos += 1
            tx_data.append([tx_dict[tk]
                            for tk in blockchain_transaction_keys.keys()])
        return tx_data

    def __select(self, sql, cursor_factory=RealDictCursor):
        response = {}
        try:
            # logger.info(sql)
            cursor = self.__conn.cursor(cursor_factory=cursor_factory)
            cursor.execute(sql)
            response = cursor.fetchall()
        except Exception:
            logger.error('>>> __select', exc_info=True)
        return response

    def __persist(self, sql, data, is_batch=False, page_size=3000):
        try:
            cursor = self.__conn.cursor()
            if is_batch:
                execute_batch(cursor, sql, data, page_size=page_size)
            else:
                cursor.execute(sql, data)
            self.__conn.commit()
        except Exception:
            logger.error('>>> __persist', exc_info=True)
