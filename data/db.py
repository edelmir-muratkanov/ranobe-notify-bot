import sqlite3


class Database:
    def __init__(self, dbname='data.db') -> None:
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        sql = "CREATE TABLE IF NOT EXISTS sources(chat_id INTEGER, name TEXT UNIQUE, url TEXT, last_chapter_num INTEGER)"
        self.conn.execute(sql)
        self.conn.commit()

    def add(self, chat_id: int, name: str, url: str, last_chapter_num: int = 0):
        sql = "INSERT INTO sources (chat_id, name, url, last_chapter_num) VALUES (?, ?, ?, ?)"
        args = (chat_id, name, url, last_chapter_num)
        self.conn.execute(sql, args)
        self.conn.commit()

    def delete(self, chat_id: int, name: str):
        sql = "DELETE FROM sources WHERE name = (?) AND chat_id = (?)"
        args = (name, chat_id)
        self.conn.execute(sql, args)
        self.conn.commit()

    def update(self, chat_id: int, name: str, url: str, last_chapter_num: int):
        sql = "UPDATE sources SET url = (?), last_chapter_num = (?) WHERE name = (?) AND chat_id = (?)"
        args = (url, last_chapter_num, name, chat_id)
        self.conn.execute(sql, args)
        self.conn.commit()

    def get_all(self, chat_id: int | None):
        if chat_id is not None:
            sql = "SELECT * FROM sources WHERE chat_id = (?)"
            args = (chat_id, )
            return [x for x in self.conn.execute(sql, args)]
        else:
            sql = "SELECT * FROM sources"
            return [x for x in self.conn.execute(sql)]

    def get(self, chat_id: int,  name: str):
        sql = "SELECT * FROM sources WHERE name = (?) AND chat_id = (?)"
        args = (name, chat_id)
        return [self.conn.execute(sql, args)]


if __name__ == '__main__':
    db = Database()
    print(db.get_all())
