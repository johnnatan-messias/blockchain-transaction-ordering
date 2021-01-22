import traceback
import requests



class BTC_Com:

    def __init__(self):
        self.api_url = 'https://pushtx.btc.com/api/tree?txhash={txid}'

        self.headers = {
            'Content_Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"'
        }

    def get_info(self, txid):
        url = self.api_url.format(txid=txid)
        ans = {}
        nerr = 0
        try:
            while nerr < 2:
                rq = requests.get(url, headers=self.headers, timeout=30)
                if rq.status_code != 200:
                    nerr += 1
                else:
                    ans = rq.json()
                    break
                rq.connection.close()
        except Exception:
            print(traceback.print_exc())

        return ans

    def getHeader(self):
        return self.headers

    def setHeader(self, header):
        self.headers = header


if __name__ == "__main__":
    txid = '90b309f445c7c630dfd42ceb1cc461fb24648fe62a9bc1563d2e7a3c3a0b8af5'
    api = BTC_Com()
    info = api.get_info(txid=txid)
    print(info)
