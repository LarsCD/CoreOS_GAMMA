from src.engine.file_management.gamma_coder import Gamma_coder

if __name__ == "__main__":
    # begin
    gamma_module = Gamma_coder()
    key = gamma_module.generate_key()

    data = 'Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello ' \
           'there Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello there ' \
           'Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello ' \
           'there Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello there ' \
           'Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello ' \
           'there Hello there Hello there Hello there Hello there Hello there Hello there Hello there Hello there '

    print(f'data: {data}')
    print(f'key: {key}')

    encrypted_data = gamma_module.encrypt_data(data, key)
    print(f'encrypted_data: {encrypted_data}')
    decrypted_data = gamma_module.decrypt_data(encrypted_data, key)
    print(f'decrypted_data: {decrypted_data}')

    gamma_module.write_encrypted_file_data(data, key, 'test2')
    decrypted_data = gamma_module.read_encrypted_file_data(key, 'test2')
    print(f'file decrypted_data: {decrypted_data}')



