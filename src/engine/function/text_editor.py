import logging

from src.engine.logger.dev_logger import DevLogger
from src.display.GUT_2 import GUT


class Texteditor:
    def __init__(self):
        # preferences
        self.log = DevLogger(Texteditor).log
        self.GUT = GUT()

        self.current_loaded_data: dict = {
            "text_list": [["#TEST TEXT#"], ["#TEXT TEST#"]],
            "file_name": "testfile.cos",
            "line_count": 2
        }
        self.editor_mode = "ADD TEXT"

    def editor_loop(self):
        while True:
            self.GUT.clear_screen()
            formatted_text = self.format_list_to_str(self.current_loaded_data["text_list"])
            self.GUT.draw_line()
            self.GUT.draw_title(self.current_loaded_data["file_name"])

            print(formatted_text)

            self.GUT.draw_bar_text(f"[LINE: # ({self.current_loaded_data['line_count']} LINES) | \"/complete\" to save]")

            entry = self.GUT.input_entry(text=f"[{self.editor_mode}] ")
            self.current_loaded_data["text_list"].append([f"{entry}"])
            if entry == "/complete":
                break

    @staticmethod
    def format_str_to_list(self, string):
        string_list = string.strip().split('\n')
        return [string_list]

    def format_list_to_str(self, string_list):
        formatted_string: str = f""

        for line in string_list:
            string_line = f"{self.GUT.settings['char']} {line[0]}\n"
            # TODO: Fix the fact that one line is not covered by a 'char'
            formatted_string += string_line


        return formatted_string

    @staticmethod
    def update_editor_metadata(self):  # TODO: Update method to update line count etc.
        pass

    def import_text(self, data):  # TODO: Update method
        try:
            text_string = str(data["text"])
        except TypeError:
            self.log(logging.ERROR, "import text string is not string")
        else:
            self.current_loaded_data["text_list"].append([f"{text_string}"])
