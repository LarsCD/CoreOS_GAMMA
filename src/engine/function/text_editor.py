import logging

from src.engine.logger.dev_logger import DevLogger
from src.display.GUT_2 import GUT
from src.engine.file_management.file_IO import FileIO


class Texteditor:
    def __init__(self):
        # preferences
        self.log = DevLogger(Texteditor).log
        self.GUT = GUT()

        self.current_loaded_data: dict = {
            "text_list": [["#TEST TEXT#"], ["#TEXT TEST#"]],
            "file_name": "testfile.cos",
            "line_count": 2,
            "saved_data": None,
        }
        self.editor_mode = "ADD TEXT"

    def load_textlist_from_file(self, loaded_editor_data):
        # check if user wants to write to line
        self.GUT.draw_warning(f'Are you sure you want to load this data? (data: {loaded_editor_data["file_name"]})')
        # line_index + 1 because it's the number that shows up in the editor
        user_input = self.GUT.input_entry('[Y/n]')

        if user_input == 'n' or user_input == 'N' or user_input == 'no' or user_input == 'No':
            return
        else:
            self.current_loaded_data = loaded_editor_data


    def editor_loop(self):
        # Apologies Lars in advance, this is probs going to be a shit method, fix or live with the consequences :3
        # Update: who made this mess...
        # TODO: Bro succes man...
        def line_index_input(text='Input at line', index_mode=False):
            try:
                line_index: int = int(self.GUT.input_entry(text))
                if not index_mode:
                    line_index -= 1
            except ValueError:
                self.GUT.click_error('Line input must be of type: \'int\'')
                return None
            if line_index - 1 > len(self.current_loaded_data['text_list']) or line_index - 1 < 0:
                # line_index NOT valid
                if not index_mode:
                    line_index += 1
                self.GUT.click_error(f'Line {line_index} does not exist')
                return None
            else:
                return line_index

        def text_input(text=''):
            try:
                text_str_input: str = self.GUT.input_entry(text)
            except ValueError:
                self.GUT.click_error('Text input must be of type: \'str\'')
                return None
            else:
                return text_str_input

        def edit_mode(self: Texteditor):
            # check if input valid
            line_index: int = line_index_input()
            if line_index is None:
                return

            text_str_input: str = text_input()
            if text_str_input is None:
                return

            # check if user wants to write to line
            self.GUT.draw_warning(f'Are you sure you want to overwrite this line? (line: {line_index})')
            # line_index + 1 because it's the number that shows up in the editor
            user_input = self.GUT.input_entry('[Y/n]')

            if user_input == 'n' or user_input == 'N' or user_input == 'no' or user_input == 'No':
                return
            else:
                self.current_loaded_data['text_list'][line_index][0] = text_str_input

        def insert_mode(self: Texteditor):
            line_index: int = line_index_input(text="Insert at line")
            if line_index is None:
                return

            text_str_input: str = text_input()
            if text_str_input is None:
                return

            self.current_loaded_data['text_list'].insert(line_index, [text_str_input])

        def command_manager(self: Texteditor):
            entry = self.GUT.input_entry(text=f"")
            if entry == "/s":
                return 1
            elif entry == "/e":
                edit_mode(self)
                return 0
            elif entry == "/i":
                insert_mode(self)
                return 0
            elif entry == "/exit":
                return -1
            elif entry == "/debug":
                print(self.current_loaded_data)
            else:
                self.current_loaded_data["text_list"].append([f"{entry}"])

        # EDITOR LOOP
        while True:
            self.update_editor_metadata(self)
            self.GUT.clear_screen()
            formatted_text = self.format_list_to_str(self.current_loaded_data["text_list"])
            self.GUT.draw_line()
            self.GUT.draw_title(self.current_loaded_data["file_name"])

            print(formatted_text)

            self.GUT.draw_bar_text(
                f"[{self.current_loaded_data['line_count']} LINES | \"/e\" to edit | \"/i\" to insert | \"/s\" to "
                f"save | \"/e\" to exit]")

            # manage text & commands input
            exit_code = command_manager(self)

            # TODO: why tf is command manager not integrated
            #  with exit_code and just dumped into the loop?? > FIX!!

            # exit loop break
            if exit_code == 1:
                # exit and save
                return self.current_loaded_data
            if exit_code == -1:
                # exit and dont save
                return None
            # exit code 0 = keep loop going

    @staticmethod
    def format_str_to_list(string):  # TODO: Probs doesn't work > fix!
        string_list = string.strip().split('\n')
        return [string_list]

    def format_list_to_str(self, string_list):
        formatted_string: str = f""

        for i, line in enumerate(string_list):
            string_line = f"{self.GUT.settings['char']} {str(f'{i + 1}').zfill(3)} |{line[0]}\n"
            # TODO: Fix the fact that one line is not covered by a 'char'
            formatted_string += string_line

        return formatted_string

    @staticmethod
    def update_editor_metadata(self):  # TODO: Update method to update line count etc.
        self.current_loaded_data["line_count"] = len(self.current_loaded_data["text_list"])
        self.log(logging.DEBUG, "Updated \"line_count\" ")

    def import_text(self, data):  # TODO: Update method
        try:
            text_string = str(data["text"])
        except TypeError:
            self.log(logging.ERROR, "import text data is not data")
        else:
            self.current_loaded_data["text_list"].append([f"{text_string}"])
