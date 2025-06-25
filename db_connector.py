import sqlite3
from project_api.wrapper_for_argon import ArgonHasher

class DatabaseConnector:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.hasher = ArgonHasher()

    def get_connection(self):
        conn = sqlite3.connect(self.filepath)
        conn.row_factory = sqlite3.Row
        return conn

    def insert_user(self, name, surname, login, password):
        try:
            hashed_password = self.hasher.hash(password)
            print(f"[DEBUG] Generated hash: {hashed_password}")
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO webUsers (name, surname, login, hash_password) VALUES (?, ?, ?, ?)",
                    (name, surname, login, hashed_password)
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"[ERROR] Failed to insert user: {e}")
            return False

    def login(self, tryLogin, tryPassword):
        with self.get_connection() as conn: 
            cursor = conn.cursor()
            cursor.execute(
                "SELECT hash_password FROM webUsers WHERE login = ?", 
                (tryLogin,)
            )
            res = cursor.fetchall()
            if len(res) == 1:
                return self.hasher.verify(res[0][0], tryPassword)
            return False

    def insert_tg_post(self, source, date, header, keyWords, message, author):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO tgParsing 
                (source, date, header, keyWords, message, author) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                (source, date, header, keyWords, message, author)
            )
            conn.commit()
            return True

    def insert_web_post(self, source, date, header, keyWords, message, author):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO tgParsing 
                (source, date, header, keyWords, message, author) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                (source, date, header, keyWords, message, author)
            )
            conn.commit()
            return True