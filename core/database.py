# SQLite database management code

import sqlite3

# Database connection

class DatabaseManager:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self, create_table_sql):
        self.cursor.execute(create_table_sql)

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()