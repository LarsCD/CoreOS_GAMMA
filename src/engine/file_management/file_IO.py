import logging
import os.path
import pathlib

from data.config.config_settings import DEFAULT_FILE_SETTINGS
from src.engine.logger.dev_logger import DevLogger
from src.engine.file_management.encryption import Encryption


class FileIO:
    def __init__(self):

        self.log = DevLogger(FileIO).log
        self.cwd = os.getcwd()
        self.Encryption = Encryption()

    @staticmethod
    def check_if_file_exists(self, full_path):
        check_bool = pathlib.Path(full_path).is_file()
        return check_bool

    def write_file(self, data, output_file, path=DEFAULT_FILE_SETTINGS['file_path']):
        """
        Write string to file in default folder 'files'

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
                self.log(logging.DEBUG, f'writing string to \'{output_file}\'')
                f.write(data)
        except Exception as e:
            self.log(logging.ERROR, f'problem with writing string to \'{output_file}\': {e}')

    def read_file(self, input_file, path=DEFAULT_FILE_SETTINGS['file_path']):
        """
        Read string from file in default folder 'files'

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
                self.log(logging.DEBUG, f'reading string from \'{input_file}\'')
                data = f.read()
        except Exception as e:
            self.log(logging.ERROR, f'problem with reading string from \'{input_file}\': {e}')

        return data

    def write_encrypted_file_data(self, data, key, output_file, custom_path=None):
        self.log(logging.INFO, f'writing encrypted string to \'{output_file}\'...')

        # check if string is datatype string
        if type(data) is not str:
            self.log(logging.ERROR, f'could not write string to \'{output_file}\': string type is not string')
            return None

        encrypted_data = self.Encryption.encrypt_string(data, key)
        try:
            self.write_file(encrypted_data, output_file, path=custom_path)
        except Exception as e:
            self.log(logging.ERROR, f'could not write string to \'{output_file}\': {e}')
        else:
            self.log(logging.INFO, f'writing encrypted string to \'{output_file}\' successful! ')

    def read_encrypted_file_data(self, key, input_file, custom_path=None):
        self.log(logging.INFO, f'reading encrypted string from \'{input_file}\'...')

        raw_data = self.read_file(input_file, path=custom_path)
        decrypted_data = self.Encryption.decrypt_data(raw_data, key)
        if decrypted_data is None:
            self.log(logging.ERROR, f'could not read string from \'{input_file}\'')
        else:
            self.log(logging.INFO, f'reading encrypted string from \'{input_file}\' successful! ')
            return decrypted_data
