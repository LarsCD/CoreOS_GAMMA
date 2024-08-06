from src.engine.file_management.encryptionmanager import EncryptionManager
from src.engine.file_management.file_IO import FileIO
from src.engine.auth.authorizer import Authorizer
from src.engine.function.text_editor import Texteditor

if __name__ == "__main__":
    EncryptionManager = EncryptionManager()
    key = EncryptionManager.generate_key()
    FileIO = FileIO()
    Authorizer = Authorizer()

    password = 'password'
    key_1_pass = EncryptionManager.generate_key(password=password)

    editor_data = Texteditor().editor_loop()
    FileIO.write_encrypted_file_data(editor_data, key_1_pass, 'test_editor_file')

    loaded_editor_data = FileIO.read_encrypted_file_data(key_1_pass, 'test_editor_file')
    EDITOR = Texteditor()
    EDITOR.load_textlist_from_file(loaded_editor_data)
    EDITOR.editor_loop()
