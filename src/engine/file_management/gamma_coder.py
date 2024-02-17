import logging
import os.path

from cryptography.fernet import Fernet

from src.engine.logger.dev_logger import DevLogger
from src.engine.file_management.file_IO import fileIO


class Gamma_coder:
    def __init__(self):
        self.log = DevLogger(Gamma_coder).log
        self.cwd = os.getcwd()
        self.fileIO = fileIO()

    @staticmethod
    def generate_key():
        """
        Generate a key for encryption and decryption
        """
        return Fernet.generate_key()

    def encrypt_data(self, data, key):
        """
        Encrypt data using a provided key
        """
        self.log(logging.DEBUG, f'encrypting data...')

        encrypted_data = None

        try:
            bytes_data = data.encode('utf-8')
            cipher_suite = Fernet(key)
            encrypted_data = cipher_suite.encrypt(bytes_data)
        except Exception as e:
            self.log(logging.ERROR, f'problem with encrypting data: {e}')
        else:
            self.log(logging.DEBUG, f'successfully encrypted data')

        return encrypted_data

    def decrypt_data(self, data, key):
        """
        Decrypt data using a provided key
        """

        self.log(logging.DEBUG, f'decrypting data...')

        try:
            cipher_suite = Fernet(key)
            decrypted_data = cipher_suite.decrypt(data)
            data = decrypted_data.decode('utf-8')
        except Exception as e:
            self.log(logging.ERROR, f'problem with decrypting data: {e}')
        else:
            self.log(logging.DEBUG, f'successfully decrypted data')

        return data

    def write_encrypted_file_data(self, data, key, output_file, custom_path=None):
        self.log(logging.INFO, f'writing encrypted data to \'{output_file}\'...')

        encrypted_data = self.encrypt_data(data, key)
        self.fileIO.write_file(encrypted_data, output_file, path=custom_path)
        self.log(logging.INFO, f'writing encrypted data to \'{output_file}\' successful! ')

    def read_encrypted_file_data(self, key, input_file, custom_path=None):
        self.log(logging.INFO, f'reading encrypted data from \'{input_file}\'...')

        raw_data = self.fileIO.read_file(input_file, path=custom_path)
        decrypted_data = self.decrypt_data(raw_data, key)
        self.log(logging.INFO, f'reading encrypted data from \'{input_file}\' successful! ')
        return decrypted_data
