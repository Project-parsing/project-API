import sqlite3
from wrapper_for_argon import ArgonHasher


class DatabaseConnector:
    def __init__(self, filepath: str):
        self.con = sqlite3.connect(filepath)
        self.cursor = self.con.cursor()
        self.hasher = ArgonHasher()

    def insert_user(self, name, surname, patronymic, login, password, filepath):
        hashed_password = self.hasher.hash(password)
        information = (name, surname, patronymic, login, hashed_password, filepath)
        self.cursor.execute("INSERT INTO tgParsing (name, surname, patronymic, login, hash_password) VALUES (?,?,?,?,?,?)", information )
        self.con.commit()
        return True

    def login(self, tryLogin, tryPassword):
        self.cursor.execute("SELECT hash_password FROM webUsers WHERE  login = ? ", (tryLogin))
        res = self.cursor.fetchall()
        if len(res) > 0:
            return self.hasher.verify(self, res[0], tryPassword)
        else:
            return False

    def insert_tg_post(self):
        return False

    def insert_web_post(self):
        return False

def main():
    db_executor = DatabaseClient("db.db")
    db_executor.insert_tg_post()
