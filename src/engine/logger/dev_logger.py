import logging
import os
from datetime import datetime

from data.config.config_settings import DEV_SETTINGS

time_start = datetime.today()

logger_enabled = DEV_SETTINGS['logging_enabled']


class DevLogger:
    def __init__(self, logging_class, log_level=logging.DEBUG, print_level=logging.INFO):
        self.logger_enabled = logger_enabled
        self.cwd = os.getcwd()
        self.logging_dir = DEV_SETTINGS['logging_dir']

        logging.basicConfig(level=print_level)
        logger_name = str(logging_class.__name__)
        log_file_path = str(
            f"{self.cwd}/{self.logging_dir}/dev-log-{time_start.date()}-{time_start.time().hour}h-{time_start.time().minute}m-{time_start.time().second}s.txt")

        self.logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(level=log_level)
        formatter = logging.Formatter("[%(levelname)s][%(asctime)s]: %(name)s > %(message)s")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log(self, level, message):
        if self.logger_enabled:
            self.logger.log(level, message)
