from src.engine.file_management.encryptionmanager import EncryptionManager
from src.engine.file_management.file_IO import FileIO
from src.engine.function.text_editor import Texteditor
from src.engine.auth.authorizer import Authorizer

if __name__ == "__main__":
    EncryptionManager = EncryptionManager()
    key = EncryptionManager.generate_key()
    FileIO = FileIO()
    Authorizer = Authorizer()

    data = 'Hello there'
    password = 'password'
    key_1_pass = EncryptionManager.generate_key(password=password)
    key_2_pass = EncryptionManager.generate_key(password=password)

    # print(f'data: {data}')
    # print(f'key: {key}')
    # print(f'key_1_pass: {key_1_pass}')
    # print(f'key_2_pass: {key_2_pass}')
    #
    # encrypted_data = EncryptionManager.encrypt_data(data, key_1_pass)
    # print(f'encrypted_data: {encrypted_data}')
    # decrypted_data = EncryptionManager.decrypt_data(encrypted_data, key_1_pass)
    # print(f'decrypted_data: {decrypted_data}')
    #
    # FileIO.write_encrypted_file_data(data, key_2_pass, 'test2')
    # decrypted_data = FileIO.read_encrypted_file_data(key_2_pass, 'test2')
    # print(f'file decrypted_data: {decrypted_data}')
    #
    # datastruct = ['text']
    # FileIO.write_encrypted_file_data(datastruct, key_2_pass, 'data')
    # decrypted_data_2 = FileIO.read_encrypted_file_data(key_2_pass, 'data')
    # print(f'file (data) decrypted_data: {decrypted_data_2}')
    #
    editor_data = Texteditor().editor_loop()
    FileIO.write_encrypted_file_data(editor_data, key_1_pass, 'test_editor_file')
    #
    # decrypted_data_text = FileIO.read_encrypted_file_data(key_2_pass, 'test_editor_file')
    # print(decrypted_data_text)

    password = 'password123'
    check_key = EncryptionManager.generate_key(password=password)
    Authorizer.save_pass_key(check_key, 'check_password')
    is_password = Authorizer.check_password(password, 'check_password')
