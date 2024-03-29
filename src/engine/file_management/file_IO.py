import logging
import os.path
import pathlib
from os.path import dirname, abspath

from data.config.config_settings import DEFAULT_FILE_SETTINGS
from src.engine.logger.dev_logger import DevLogger
from src.engine.file_management.encryptionmanager import EncryptionManager


class FileIO:
    def __init__(self):
        self.log = DevLogger(FileIO).log
        self.cwd = dirname(dirname(dirname(dirname(abspath(__file__)))))
        self.Encryption = EncryptionManager()

    @staticmethod
    def check_if_file_exists(self, full_path):
        check_bool = pathlib.Path(full_path).is_file()
        return check_bool

    def write_file(self, data, output_file, path=DEFAULT_FILE_SETTINGS['file_path'],
                   extension=DEFAULT_FILE_SETTINGS['file_extension']):
        """
        Write data to file in default folder 'files'

        :param extension:
        :param data:
        :param output_file:
        :param path:
        :return:
        """

        # in case of given path is None, use default file settings
        if path is None:
            path = DEFAULT_FILE_SETTINGS['file_path']

        full_path = None

        file_path = os.path.join(path, output_file)
        full_path = f"{self.cwd}{file_path}{extension}"
        self.log(logging.DEBUG, f'full_path=\'{full_path}\'')

        read_setting = 'wb'

        # check if data being written is of type byte or data
        if isinstance(data, str):
            read_setting = 'w'

        with open(full_path, read_setting) as f:
            self.log(logging.DEBUG, f'writing data to \'{output_file}\'')
            f.write(data)

    def read_file(self, input_file, path=DEFAULT_FILE_SETTINGS['file_path'], extension=DEFAULT_FILE_SETTINGS['file_extension']):
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

        file_path = os.path.join(path, input_file)
        full_path = f"{self.cwd}{file_path}"
        self.log(logging.DEBUG, f'full_path=\'{full_path}\'')

        with open(f"{full_path}{extension}", 'rb') as f:
            self.log(logging.DEBUG, f'reading data from \'{input_file}\'')
            data = f.read()
        return data

    def write_encrypted_file_data(self, data, key, output_file, custom_path=None):
        self.log(logging.INFO, f'writing encrypted data to \'{output_file}\'...')

        encrypted_data = self.Encryption.encrypt_data(data, key)
        self.write_file(encrypted_data, output_file, path=custom_path)

    def read_encrypted_file_data(self, key, input_file, custom_path=None):
        self.log(logging.INFO, f'reading encrypted data from \'{input_file}\'...')

        raw_data = self.read_file(input_file, path=custom_path)
        decrypted_data = self.Encryption.decrypt_data(raw_data, key)
        if decrypted_data is None:
            self.log(logging.ERROR, f'could not read data from \'{input_file}\'')
        else:
            self.log(logging.INFO, f'reading encrypted data from \'{input_file}\' successful! ')
            return decrypted_data
