import logging
import os

import yaml

from .application_paths import ApplicationPaths


class LoggerFactory:

    @staticmethod
    def get_logger(module_name=None):
        # Get Configuration file path
        os.makedirs(name=ApplicationPaths.logs(), exist_ok=True)
        logging.config.dictConfig(
            yaml.load(open(ApplicationPaths.config('logging.yaml'), 'r'), Loader=yaml.SafeLoader))

        if module_name:
            return logging.getLogger(module_name)
        return logging.getLogger()
