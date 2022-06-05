from sqlalchemy import MetaData, PrimaryKeyConstraint, create_engine, Table, Column, String, Integer
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)

metadata = MetaData()

sources = Table(
    'sources',
    metadata,
    Column('chat_id', Integer()),
    Column('name', String(200)),
    Column('url', String(200)),
    Column('last_num', Integer(), default=0),
    PrimaryKeyConstraint('chat_id', 'name', name='sources_pk')
)


class Database:
    def __init__(self) -> None:
        self.conn = engine.connect()

    def setup(self):
        metadata.create_all(engine)

    def add(self, chat_id: int, name: str, url: str, last_num: int = 0):
        q = sources.insert().values((chat_id, name, url, last_num))
        r = self.conn.execute(q)

    def get_all(self, chat_id: int | None):
        q = None
        if chat_id is not None:
            q = sources.select().where(sources.c.chat_id == chat_id)
        else:
            q = sources.select()
        r = self.conn.execute(q)
        return r.fetchall()

    def get(self, chat_id: int,  name: str):
        q = sources.select().where((sources.c.chat_id == chat_id) & (sources.c.name == name))
        r = self.conn.execute(q)
        return r.fetchone()

    def update(self, chat_id: int, name: str, url: str, last_num: int):
        q = sources.update()\
            .where((sources.c.chat_id == chat_id) & (sources.c.name == name))\
            .values((chat_id, name, url, last_num))
        r = self.conn.execute(q)

    def delete(self, chat_id: int, name: str):
        q = sources.delete().where(sources.c.chat_id == chat_id & sources.c.name == name)
        r = self.conn.execute(q)
