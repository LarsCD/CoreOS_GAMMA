import logging
from os.path import dirname, abspath

from src.engine.file_management.file_IO import FileIO
from src.engine.logger.dev_logger import DevLogger
from src.engine.file_management.encryptionmanager import EncryptionManager
from data.config.config_settings import AUTH_SETTINGS


class Authorizer:
    def __init__(self):
        self.FileIO = FileIO()
        self.log = DevLogger(Authorizer).log
        self.EncryptionManager = EncryptionManager()
        self.cwd = dirname(dirname(dirname(dirname(abspath(__file__)))))

    def save_pass_key(self, key, filename):
        self.FileIO.write_file(key, filename, path=AUTH_SETTINGS['auth_key_dir'],
                               extension=AUTH_SETTINGS["file_extension"])
        self.log(logging.INFO, f'saved {filename}{AUTH_SETTINGS["file_extension"]}')

    def check_password(self, password, filename):
        self.log(logging.INFO, 'checking password')
        check_key = self.FileIO.read_file(filename, path=AUTH_SETTINGS['auth_key_dir'],
                                          extension=AUTH_SETTINGS["file_extension"])
        password_key = self.EncryptionManager.generate_key(password=password)

        if password_key == check_key:
            self.log(logging.INFO, 'password correct')
            return 1
        else:
            self.log(logging.INFO, 'password NOT correct')
            return 0
