from os import system
import colorama as col
from data.config.config_settings import DEFAULT_GUT_SETTINGS


class GUT:
    def __init__(self, SETTINGS=DEFAULT_GUT_SETTINGS):
        self.settings = SETTINGS
        self.hl_color = col.Fore.GREEN
        self.bar_fg_color = col.Fore.BLACK
        self.bar_bg_color = col.Back.LIGHTBLACK_EX
        self.rst = col.Style.RESET_ALL

        self.standard_bar_text = "[Type \'/\' for commands, \'/h\' or \'/help\' for list of commands]"

    def clear_screen(self):
        system('cls' if self.settings.get('os', 'windows') == 'windows' else 'clear')

    def draw_line(self):
        print(self.settings['char'] * self.settings['default_line_size'])

    def draw_title(self, title):
        print(f"{self.settings['char']} [{title}]")

    def draw_text(self, text):
        print(f"{self.settings['char']} {text}")

    def draw_error(self, text):
        print(f"{self.settings['char']}{col.Fore.RED} > [ERROR]: {text}{self.rst}")

    def click_text(self, text=""):
        self.draw_text(text)
        input()

    def click_error(self, text):
        self.draw_error(text)
        input()

    def input_entry(self, text=""):
        input_entry = input(f"{self.settings['char']} {text}> ")
        return input_entry

    def draw_bar_text(self, text=""):
        if text == "":
            text = self.standard_bar_text

        print(f'{self.bar_bg_color}{self.settings["char"]}{self.bar_fg_color} {text}{self.rst}')

    def draw_box(self, width, height):
        for _ in range(height):
            self.draw_line()

    def align_text(self, text, width, alignment='left'):
        if alignment == 'l':
            return text.ljust(width)
        elif alignment == 'r':
            return text.rjust(width)
        elif alignment == 'c':
            return text.center(width)
        else:
            return f"{self.settings['char']} {text}"

    def menu_select(self, title, options, text=None, bar_text="", error_text: list = []):
        self.clear_screen()
        self.draw_line()
        self.draw_title(title)
        print(f"{self.settings['char']}")
        if text:
            self.draw_text(text)
        for key, value in options.items():
            print(f'{self.settings["char"]} [{self.hl_color}{key.capitalize()}{self.rst}]: {value}')
        print(f"{self.settings['char']}")

        for line in error_text:
            print(f"{self.settings['char']}{col.Fore.RED} > [ERROR]: {line}{self.rst}")

        self.draw_bar_text(bar_text)
        user_input = input(f"{self.settings['char']} > ")
        return user_input

    def display_text(self, title, text, options=None, bar_text="", error_text: list = []):
        self.clear_screen()
        self.draw_line()
        self.draw_title(title)
        print(f"{self.settings['char']}")

        if isinstance(text, str):
            text = text.split('\n')  # Split the text into paragraphs based on newline characters

        for paragraph in text:
            lines = paragraph.split('\n')  # Split each paragraph into lines
            for line in lines:
                print(f"{self.settings['char']} {line}")  # Print each line prefixed with the desired character

        if options:
            for key, value in options.items():
                print(f'{self.settings["char"]} [{self.hl_color}{key.capitalize()}{self.rst}]: {value}')
        print(f"{self.settings['char']}")

        for line in error_text:
            print(f"{self.settings['char']}{col.Fore.RED} > [ERROR]: {line}{self.rst}")

        self.draw_bar_text(bar_text)
        user_input = input(f"{self.settings['char']} > ")
        return user_input


# Example usage:
if __name__ == "__main__":
    settings = {
        'os': 'windows',
        'char': '█',
        'default_line_size': 80
    }
    gut = GUT(settings)
    gut.clear_screen()
    gut.draw_line()
    gut.draw_title('Sample Title')
    gut.draw_text('This is a sample text.')
    # gut.draw_box(20, 5)
    options = {'a': 'Option A', 'b': 'Option B', 'c': 'Option C'}
    user_input = gut.menu_select('Menu', options, text='Please select an option:',
                                 error_text=["File \'homework.COS\' could not be saved correctly"])
    gut.display_text('TITLE', '''Wow, look at me!
Is this working
    
I think so!''', options=options)
    gut.click_error("Command could not be completed successfully")
    options2 = {'1': 'START COREOS', '2': 'SETTINGS', '3': 'EXIT'}
    gut.menu_select('COREOS GAMMA STARTUP', options2, bar_text="[For advanced config type: \'/config\']")
