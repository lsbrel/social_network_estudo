# PYTHON
import secrets

class Token:

    @staticmethod
    def generateToken():
        
        return secrets.token_hex(16)