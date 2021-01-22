import pandas as pd

from .logger_factory import LoggerFactory

logger = LoggerFactory.get_logger("logger_application")
# https://www.online-toolz.com/tools/text-hex-convertor.php


class Common:

    @staticmethod
    def to_english_number_format(x, precision=0):
        msk = '{:,.%df}' % precision
        return msk.format(x)

    @staticmethod
    def fee_rate(self, nFeePaid, nBytes, in_sat=True):
        nSize = pd.np.int64(nBytes)
        if not in_sat:
            nFeePaid = 1e8 * nFeePaid
        nSatoshisPerK = nFeePaid * 1000 / nSize
        return pd.np.int64(nSatoshisPerK)

    @staticmethod
    def identify_miner(script):
        if '2f736c7573682f' in script:
            return 'SlushPool'
        elif '2f4254432e544f502f' in script:
            return 'BTC.TOP'
        elif '2f5669614254432f' in script:
            return 'ViaBTC'
        elif '706f6f6c2e626974636f696e2e636f6d' in script:
            return 'Bitcoin.com'
        elif '2f4254432e434f4d2f' in script:
            return 'BTC.com'
        elif '416e74506f6f6c' in script:
            return 'AntPool'
        elif '2f426974436c7562204e6574776f726b2f' in script:
            return 'BitClub Network'
        elif 'f09f909f00' in script or '2f4632506f6f6c2f' in script:
            return 'F2Pool'
        elif '706f6f6c696e2e636f6d' in script:
            return 'Poolin'
        elif '2f426974636f696e2d5275737369612e72752f' in script:
            return 'BitcoinRussia'
        elif '2f426974667572792f' in script:
            return 'BitFury'
        elif '4b616e6f506f6f6c' in script:
            return 'KanoPool'
        elif '2f48756f62692f' in script or '2f48756f42692f' in script:
            return 'Huobi'
        elif '4d696e656420627920064257506f6f6c' in script:
            return 'BWPool'
        elif '2f4254504f4f4c2f' in script:
            return 'BTPool'
        elif '2f5365637265745375706572737461722f' in script:
            return 'SecretSuperstar'
        elif '2f44504f4f4c2e544f502f' in script:
            return 'DPool.TOP'
        elif '2f3538636f696e2e636f6d2f' in script:
            return '58Coin'
        elif '2f425443432f' in script:
            return 'BTCC Pool'
        elif '74696765722f7469676572706f6f6c2e6e6574' in script:
            return 'Tiger Pool'
        elif '2f45324d2026204254432e544f502f' in script:
            return 'E2M & BTC.TOP'
        elif '2f636b706f6f6c2e6f72672f' in script:
            return 'CKPool'
        elif '636b706f6f6c' in script:
            return 'CKPool'
        elif '526177706f6f6c2e636f6d2f526177706f6f6c2e636f6d2f' in script:
            return 'RawPool.com'
        elif '2f7777772e6f6b65782e636f6d2f' in script:
            return 'Okex'
        elif '2f315448617368263538434f494e2f' in script:
            return '1THash & 58COIN'
        elif '2f7461616c2e636f6d2f' in script:
            return 'Taal'
        elif '2f62797465706f6f6c2e636f6d2f' in script:
            return 'BytePool'
        elif '2f426978696e2f' in script:
            return 'Bixin'
        elif '2f5369676d61506f6f6c2e636f6d2f' in script or '2f5369676d61706f6f6c2e636f6d2f' in script:
            return 'SigmaPool'
        elif '2f42696e616e63652f' in script or '62696e616e63652e636f6d' in script:
            return 'Binance Pool'
        elif '2f6c756269616e2e636f6d2f' in script:
            return 'Lubian.com'
        elif '2f4e6f7661426c6f636b2f' in script:
            return 'NovaBlock'
        elif '2f537069646572506f6f6c' in script:
            return 'SpiderPool'
        elif '2f686173682e6f6b6b6f6e672e636f6d2f' in script:
            return 'OKKONG'
        return 'Unknown'
