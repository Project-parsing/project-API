from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError, VerificationError

class ArgonHasher:
    def __init__(self):
        self.hasher = PasswordHasher()

    def hash(self, password: str) -> str:
        return self.hasher.hash(password.encode('utf-8'))

    def verify(self, hash: str, password: str) -> bool:
        try:
            return self.hasher.verify(hash, password.encode('utf-8'))
        except (VerifyMismatchError, InvalidHashError, VerificationError) as e:
            print(f"[ERROR] Argon2 verification failed: {str(e)}")
            return False