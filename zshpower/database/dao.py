import sqlite3
from os.path import join
from zshpower.config.base import Base
from zshpower import HOME
from zshpower.database.sql import sql


class DAO(Base):
    def __init__(self):
        try:
            Base.__init__(self, HOME)
            self.conn = sqlite3.connect(self.database_path)
            self.get_cursor = self.conn.cursor()

        except sqlite3.Connection.Error:
            raise sqlite3.Connection.Error(
                "An error occurred while connecting to the database. Make sure that the SQLite database is turned on."
                "One way to resolve it is by running the command 'zshpower init [--omz]'"
            )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> sqlite3.Connection.close:
        self.commit()
        self.connection.close()

    @property
    def connection(self) -> sqlite3.Connection:
        return self.conn

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.get_cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql_, params=None):
        self.cursor.execute(sql_, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql_, params=None):
        self.cursor.execute(sql_, params or ())
        return self.fetchall()

    def query_one(self, sql_, params=None):
        self.cursor.execute(sql_, params or ())
        return self.fetchone()

    def create_table(self, tbl_name):
        try:
            self.execute(sql()[tbl_name])
            self.commit()
            self.connection.close()
            return True
        except (sqlite3.DatabaseError, sqlite3.DataError):
            return False

    def select_columns(self, /, columns=(), table=None) -> dict:
        sql_ = f"SELECT {','.join(columns)} FROM {table};"
        query = self.query(sql_)
        data = {key: value for (key, value) in query}
        self.connection.close()
        return data

    def select_where(self, table, value, where, select=()) -> list:
        sql_ = f"SELECT {','.join(select)} FROM {table} WHERE {where} = '{value}';"
        data = self.query(sql_)
        self.commit()
        self.connection.close()
        return data

    def insert(self, table, /, columns=(), values=()) -> bool:
        sql_ = f"INSERT INTO {table} {columns} VALUES {values};"
        try:
            self.execute(sql_)
            self.commit()
            self.connection.close()
            return True
        except Exception:
            raise Exception("Error insert database.")

    def update(self, table, set_, version, where, value) -> bool:
        sql_ = f"UPDATE {table} SET {set_} = '{version}' WHERE {where} = '{value}';"
        try:
            self.execute(sql_)
            self.commit()
            self.connection.close()
            return True
        except Exception:
            raise Exception("Error update database.")
