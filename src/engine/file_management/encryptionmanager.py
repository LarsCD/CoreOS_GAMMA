import logging
import os.path

import base64
import pickle

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

    def encrypt_data(self, data, key) -> bytes:
        """
        Encrypt data using a provided key
        """
        self.log(logging.DEBUG, f'encrypting data...')

        encrypted_data = None

        cipher_suite = Fernet(key)

        if not isinstance(data, str):
            data_bytes = pickle.dumps(data)
            encrypted_data = cipher_suite.encrypt(data_bytes)
        else:
            bytes_data = data.encode('utf-8')
            encrypted_data = cipher_suite.encrypt(bytes_data)

        return encrypted_data

    def decrypt_data(self, data, key):
        """
        Decrypt data using a provided key
        """

        self.log(logging.DEBUG, f'decrypting data...')

        decrypted_data = None

        cipher_suite = Fernet(key)
        decrypted_data_raw = cipher_suite.decrypt(data) # TODO: something goes wrong when decrypting the raw data > find the problem
        try:
            decrypted_data = decrypted_data_raw.decode('utf-8')
        except UnicodeDecodeError:
            decrypted_data = pickle.loads(decrypted_data_raw)

        return decrypted_data
