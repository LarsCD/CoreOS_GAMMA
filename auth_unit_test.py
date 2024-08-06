from src.engine.file_management.encryptionmanager import EncryptionManager
from src.engine.file_management.file_IO import FileIO
from src.engine.auth.authorizer import Authorizer

if __name__ == "__main__":
    EncryptionManager = EncryptionManager()
    key = EncryptionManager.generate_key()
    FileIO = FileIO()
    Authorizer = Authorizer()

    password = 'password123'
    check_key = EncryptionManager.generate_key(password=password)
    Authorizer.save_pass_key(check_key, 'check_password')
    is_password = Authorizer.check_password(password, 'check_password')
    input()