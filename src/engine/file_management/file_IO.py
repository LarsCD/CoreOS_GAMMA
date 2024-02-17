import logging
import os.path

from data.config.config_settings import DEFAULT_FILE_SETTINGS
from src.engine.logger.dev_logger import DevLogger


class fileIO:
    def __init__(self):
        self.log = DevLogger(fileIO).log
        self.cwd = os.getcwd()

    def write_file(self, data, output_file, path=DEFAULT_FILE_SETTINGS['file_path']):
        """
        Write data to file in default folder 'files'

        :param data:
        :param output_file:
        :param path:
        :return:
        """

        # in case of given path is None, use default file settings
        if path is None:
            path = DEFAULT_FILE_SETTINGS['file_path']

        full_path = None

        try:
            file_path = os.path.join(path, output_file)
            full_path = f"{self.cwd}{file_path}{DEFAULT_FILE_SETTINGS['file_extension']}"
            self.log(logging.DEBUG, f'full_path=\'{full_path}\'')
        except Exception as e:
            self.log(logging.ERROR, f'problem finding path for \'{output_file}\' to write to: {e}')

        try:
            with open(full_path, 'wb') as f:
                self.log(logging.DEBUG, f'writing data to \'{output_file}\'')
                f.write(data)
        except Exception as e:
            self.log(logging.ERROR, f'problem with writing data to \'{output_file}\': {e}')

    def read_file(self, input_file, path=DEFAULT_FILE_SETTINGS['file_path']):
        """
        Read data from file in default folder 'files'

        :param input_file:
        :param path:
        :return:
        """

        # in case of given path is None, use default file settings
        if path is None:
            path = DEFAULT_FILE_SETTINGS['file_path']

        full_path = None
        data = None

        try:
            file_path = os.path.join(path, input_file)
            full_path = f"{self.cwd}{file_path}"
            self.log(logging.DEBUG, f'full_path=\'{full_path}\'')
        except Exception as e:
            self.log(logging.ERROR, f'problem finding path for \'{input_file}\' to read from: {e}')

        try:
            with open(f"{full_path}.COS", 'rb') as f:
                self.log(logging.DEBUG, f'reading data from \'{input_file}\'')
                data = f.read()
        except Exception as e:
            self.log(logging.ERROR, f'problem with reading data from \'{input_file}\': {e}')

        return data
