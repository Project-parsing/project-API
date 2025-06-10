import sqlite3
from wrapper_for_argon import ArgonHasher


class DatabaseConnector:
    def __init__(self, filepath: str):
        self.con = sqlite3.connect(filepath)
        self.cursor = self.con.cursor()
        self.hasher = ArgonHasher()

    def insert_user(self, name, surname,  login, password):
        hashed_password = self.hasher.hash(password)
        information = (name, surname,  login, hashed_password)
        self.cursor.execute("INSERT INTO webUsers (name, surname, login, hash_password) VALUES (?,?,?,?)", information )
        self.con.commit()
        return True

    def login(self, tryLogin, tryPassword):
        self.cursor.execute("SELECT `hash_password` FROM `webUsers` WHERE `login` = ?", (tryLogin,))
        res = self.cursor.fetchall() 
        if len(res) == 1:
            return self.hasher.verify(res[0][0], tryPassword)
        else:
            return False
        

    def insert_tg_post(self, sourse, date, header, keyWords,message, author):
        information = (sourse, date, header, keyWords, message, author)
        self.cursor.execute("INSERT INTO tgParsing (sourse, date, header, keyWords, message, author) VALUES (?,?,?,?,?,?)", information )
        self.con.commit()
        return True

    def insert_web_post(self, sourse, date, header, keyWords,message, author):
        information = (sourse, date, header, keyWords, message, author)
        self.cursor.execute("INSERT INTO tgParsing (sourse, date, header, keyWords, message, author) VALUES (?,?,?,?,?,?)", information )
        self.con.commit()
        return True
