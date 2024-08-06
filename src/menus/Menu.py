import logging

from src.display.GUT_2 import GUT
from src.engine.logger.dev_logger import DevLogger


class Menu:
    def __init__(self):
        # preferences
        self.log = DevLogger(super.__name__).log
        self.GUT = GUT()
        # input
        self.commands = {
            'exit': 0,
            'debug': 10
        }

    def command_manager(self, entry):
        exit_code = self.commands[entry]
        return exit_code

