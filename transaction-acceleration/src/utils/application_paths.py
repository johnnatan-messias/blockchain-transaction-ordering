# This class summarizes all important directories of the application template,
# it's good to avoid possible mistakes when handling files.

import os


class ApplicationPaths:

    @staticmethod
    def application_root(current_path=''):
        return os.path.abspath(os.path.dirname(__file__) + os.sep + "../../") + current_path

    @staticmethod
    def config(current_path=''):
        return ApplicationPaths.application_root() + os.sep + "config/" + current_path

    @staticmethod
    def logs(current_path=''):
        return ApplicationPaths.application_root() + os.sep + "logs/" + current_path

    @staticmethod
    def dataset(current_path=''):
        return ApplicationPaths.application_root() + os.sep + "dataset/" + current_path

    @staticmethod
    def plots(current_path=''):
        return ApplicationPaths.application_root() + os.sep + "plots/" + current_path

    @staticmethod
    def makedir(path):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def makedirs():
        os.makedirs(name=ApplicationPaths.logs(), exist_ok=True)
        os.makedirs(name=ApplicationPaths.config(), exist_ok=True)
        os.makedirs(name=ApplicationPaths.dataset(), exist_ok=True)
