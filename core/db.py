import psycopg2

from core import settings


class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            port=settings.DB_PORT
        )

    def get_conn(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="your_database",
            user="your_user",
            password="your_password",
            port="5432"
        )

    def execute(self, sql, params=None, many=True):
        cursor = self.conn.cursor()

        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        result = cursor.fetchall() if many else cursor.fetchone()

        cursor.close()
        self.conn.close()

        return result

    def commit(self, sql, params=None):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        self.conn.commit()
        result = cursor.fetchone()
        self.conn.close()
        cursor.close()
        return result

