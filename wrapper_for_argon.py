import argon2

class ArgonHasher:
    def __init__(self):
        self.hasher = argon2.PasswordHasher()

    def hash(self, password: str) -> str:
        hashed_password = self.hasher.hash(password)

        return hashed_password

    def verify(self, hash: str, password: str) -> bool:
        try:
            return self.hasher.verify(hash, password)
        except argon2.exceptions.VerifyMismatchError:
            return False