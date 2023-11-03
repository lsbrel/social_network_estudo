# PYTHON
import hashlib

class SenhaHash:

    @staticmethod
    def hash(input):
        senha = hashlib.sha256(input.encode(encoding='UTF-8'))
        
        return senha.hexdigest()
