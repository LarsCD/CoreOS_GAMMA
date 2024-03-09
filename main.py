from src.engine.file_management.encryption import Encryption
from src.engine.file_management.file_IO import FileIO
from src.engine.function.text_editor import Texteditor

if __name__ == "__main__":
    Encryption = Encryption()
    key = Encryption.generate_key()
    FileIO = FileIO()

    data = 'Hello there'

    print(f'data: {data}')
    print(f'key: {key}')

    encrypted_data = Encryption.encrypt_string(data, key)
    print(f'encrypted_data: {encrypted_data}')
    decrypted_data = Encryption.decrypt_data(encrypted_data, key)
    print(f'decrypted_data: {decrypted_data}')

    FileIO.write_encrypted_file_data(data, key, 'test2')
    decrypted_data = FileIO.read_encrypted_file_data(key, 'test2')
    print(f'file decrypted_data: {decrypted_data}')

    Texteditor().editor_loop()
