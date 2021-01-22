# -*- coding: utf-8 -*-
__author__ = "Johnnatan Messias"
__copyright__ = "Max Planck Institute for Software Systems (MPI-SWS"
__email__ = "johnme@mpi-sws.org"
__website__ = "http://johnnatan.me"
__status__ = "Done"

import time

import requests

from .logger_factory import LoggerFactory

logger = LoggerFactory.get_logger('logger_application')


class BlockchainRPC:

    def __init__(self, auth, timeout=60, api_url='http://127.0.0.1:8332/', jsonrpc='2.0', rpc_id='BlockchainRPC'):
        self.__api_url = api_url
        self.timeout = timeout
        self.__headers = {
            'Content_Type': 'application/json',
        }
        self.__auth = auth
        self.__jsonrpc = jsonrpc
        self.__rpc_id = rpc_id

    def getrawmempool(self, verbose=False):
        return self.get_response(method='getrawmempool', params=[verbose])

    def getmempoolinfo(self):
        return self.get_response(method='getmempoolinfo')

    def gettransaction(self, txid, include_watchonly=False):
        return self.get_response(method='gettransaction', params=[include_watchonly])

    def getdifficulty(self):
        return self.get_response(method='getdifficulty')

    def getblockchaininfo(self):
        return self.get_response(method='getblockchaininfo')

    def getblockcount(self):
        return self.get_response(method='getblockcount')

    def getblockhash(self, height):
        return self.get_response(method='getblockhash', params=[height])

    def getbestblockhash(self):
        return self.get_response(method='getbestblockhash')

    def getblock(self, header_hash, verbosity=1):
        return self.get_response(method='getblock', params=[header_hash, verbosity])

    def getblockheader(self, header_hash, in_json=True):
        return self.get_response(method='getblockheader', params=[header_hash, in_json])

    def getblock_by_height(self, height, verbosity=1):
        block_hash = self.getblockhash(height=height)['result']
        return self.getblock(header_hash=block_hash, verbosity=verbosity)

    def estimatesmartfee(self, nblocks):
        return self.get_response(method='estimatesmartfee', params=[nblocks])

    def getmempoolentry(self, txid):
        return self.get_response(method='getmempoolentry', params=[txid])

    def getpeerinfo(self):
        return self.get_response(method='getpeerinfo')

    def getconnectioncount(self):
        return self.get_response(method='getconnectioncount')

    def getrawtransaction(self, txid, verbosity=False):
        return self.get_response(method='getrawtransaction', params=[txid, verbosity])

    def getblockshash(self, heights):
        return map(self.getblockhash, heights)

    def getblocks(self, headers_hash, verbosity=1):
        return map(lambda header_hash: self.getblock(header_hash=header_hash, verbosity=verbosity), headers_hash)

    def getblocks_by_height(self, heights, verbosity=1):
        return map(lambda height: self.getblock_by_height(height, verbosity=verbosity), heights)

    def getblocktemplate(self):
        return self.get_response(method='getblocktemplate')

    def getmininginfo(self):
        return self.get_response(method='getmininginfo')

    def getdecodescript(self, hex_encoded):
        return self.get_response(method='decodescript', params=[hex_encoded])

    def getnetworkinfo(self):
        return self.get_response(method='getnetworkinfo')

    def get_response(self, method, params=[]):
        payload = {'jsonrpc': self.__jsonrpc, 'id': self.__rpc_id,
                   'method': method, 'params': params}
        ans = {}
        nerr = 5
        while nerr > 0:
            try:
                rq = requests.post(self.__api_url, headers=self.__headers,
                                   auth=self.__auth, json=payload, timeout=self.timeout)
                if rq.status_code == 200:
                    ans = rq.json()
                    rq.connection.close()
                    break
            except:
                logger.error("Error on BlockchainRPC", exc_info=True)
                time.sleep(1)
            nerr -= 1
        return ans

    def getHeader(self):
        return self.headers

    def setHeader(self, header):
        self.headers = header
