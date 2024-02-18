import logging
import os.path

from cryptography.fernet import Fernet

from src.engine.logger.dev_logger import DevLogger


class Encryption:
    def __init__(self):
        self.log = DevLogger(Encryption).log
        self.cwd = os.getcwd()

    @staticmethod
    def generate_key():
        """
        Generate a key for encryption and decryption
        """
        return Fernet.generate_key()

    def encrypt_string(self, string, key):
        """
        Encrypt string using a provided key
        """
        self.log(logging.DEBUG, f'encrypting string...')

        encrypted_data = None

        try:
            bytes_data = string.encode('utf-8')
            cipher_suite = Fernet(key)
            encrypted_data = cipher_suite.encrypt(bytes_data)
        except Exception as e:
            self.log(logging.ERROR, f'problem with encrypting string: {e}')
        else:
            self.log(logging.DEBUG, f'successfully encrypted string')

        return encrypted_data

    def decrypt_data(self, data, key):
        """
        Decrypt string using a provided key
        """

        self.log(logging.DEBUG, f'decrypting string...')

        decrypted_data = None

        try:
            cipher_suite = Fernet(key)
            decrypted_data_raw = cipher_suite.decrypt(data)
            decrypted_data = decrypted_data_raw.decode('utf-8')
        except Exception as e:
            print(e)
            self.log(logging.ERROR, f'problem with decrypting string: {e}')
        else:
            self.log(logging.DEBUG, f'successfully decrypted string')

        return decrypted_data

