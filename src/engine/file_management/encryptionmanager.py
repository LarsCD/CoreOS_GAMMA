import logging
import os.path

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from src.engine.logger.dev_logger import DevLogger


class EncryptionManager:
    def __init__(self):
        self.log = DevLogger(EncryptionManager).log
        self.cwd = os.getcwd()

    @staticmethod
    def generate_key(password=None) -> bytes:
        """
        Generate a key for encryption and decryption.
        If password is provided, derive the key from the password using PBKDF2.
        """
        if password:
            password = password.encode()  # Convert password to bytes
            salt = b'salt_12345'  # Salt should be unique and random for each key
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,  # Length of the key
                salt=salt,
                iterations=100000,  # Number of iterations, can be adjusted for security
                backend=default_backend()
            )
            key = kdf.derive(password)
            key = base64.urlsafe_b64encode(key)  # Encode key to base64 and make it URL-safe
        else:
            key = Fernet.generate_key()
        return key

    def encrypt_string(self, string, key):
        """
        Encrypt string using a provided key
        """
        self.log(logging.DEBUG, f'encrypting string...')

        encrypted_data = None

        # try:
        bytes_data = string.encode('utf-8')
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(bytes_data)
        # except Exception as e:
            # self.log(logging.ERROR, f'problem with encrypting string: {e}')
        # else:
            # self.log(logging.DEBUG, f'successfully encrypted string')

        return encrypted_data

    def decrypt_data(self, data, key):
        """
        Decrypt string using a provided key
        """

        self.log(logging.DEBUG, f'decrypting string...')

        decrypted_data = None

        # try:
        cipher_suite = Fernet(key)
        decrypted_data_raw = cipher_suite.decrypt(data)
        decrypted_data = decrypted_data_raw.decode('utf-8')
        # except Exception as e:
            # print(e)
            # self.log(logging.ERROR, f'problem with decrypting string: {e}')
        # else:
            # self.log(logging.DEBUG, f'successfully decrypted string')

        return decrypted_data
