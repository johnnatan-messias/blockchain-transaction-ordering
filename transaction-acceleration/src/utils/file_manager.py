import gzip
import json
import os

import pandas as pd
from tqdm import tqdm

from .application_paths import ApplicationPaths
from .logger_factory import LoggerFactory

logger = LoggerFactory.get_logger("logger_application")


class FileManager:

    @staticmethod
    def get_filenames(path, startswith='', file_format='.json.gz'):
        filenames = [filename for filename in os.listdir(
            path) if filename.startswith(startswith) and filename.endswith(file_format)]
        return filenames

    @staticmethod
    def makedir(path):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def file_exists(filename):
        return os.path.isfile(filename)

    @staticmethod
    def load_json(filename, compression=True):
        logger.info("START: Load json=%s" %
                    ApplicationPaths.dataset() + filename)
        file = gzip.open if compression else open
        data = list()
        inFile = file(ApplicationPaths.dataset() + filename, 'rt')
        pbar = tqdm(desc='Reading Json File', ascii=True)
        for line in inFile:
            data.append(json.loads(line))
            pbar.update(1)
        inFile.close()
        pbar.close()
        logger.info("DONE: Load json=%s" %
                    ApplicationPaths.dataset() + filename)
        return data

    @staticmethod
    def dump_raw_json(data, filename, compression=True):
        logger.info("START: Persist json=%s" % filename)
        file = gzip.open if compression else open
        with file(ApplicationPaths.dataset() + filename, 'wt') as file_:
            json.dump(data, file_)
        logger.info("DONE: Persist json=%s" % filename)

    @staticmethod
    def dump_json(data, filename, compression=True):
        logger.info("START: Persist json=%s" % filename)
        file = gzip.open if compression else open
        outFile = file(ApplicationPaths.dataset() + filename, 'wt')
        pbar = tqdm(desc="Persisting Json", total=len(data), ascii=True)
        count = 0
        for d in data:
            outFile.write("%s\n" % json.dumps(d))
            pbar.update(1)
            count += 1
        outFile.close()
        pbar.close()
        logger.info(f"In total {count} data were persisted")
        logger.info("DONE: Persist json=%s" % filename)

    @staticmethod
    def yield_json_file(filename, compression=True):
        file = gzip.open if compression else open
        inFile = file(filename, 'rt')
        for line in inFile:
            yield json.loads(line)
        inFile.close()

    @staticmethod
    def load_dataframe(filename, usecols=None, nrows=None, sep=';', compression='gzip'):
        logger.info("START: Load dataframe=%s" %
                    ApplicationPaths.dataset() + filename)
        df = pd.read_csv(ApplicationPaths.dataset() +
                         filename, usecols=usecols, nrows=nrows, sep=sep, compression=compression)
        logger.info("DONE: Load dataframe=%s" %
                    ApplicationPaths.dataset() + filename)
        return df

    @staticmethod
    def dump_dataframe(dataframe, filename, sep=';', index=False, compression='gzip'):
        logger.info(
            f"START: Dump {dataframe.shape[0]} registers into file=%s" % filename)
        dataframe.to_csv(ApplicationPaths.dataset() + filename,
                         sep=sep, index=index, compression=compression)
        logger.info(f"DONE: Dump dataframe=%s" % filename)
