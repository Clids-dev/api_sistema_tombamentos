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
        return psycopg2.connect(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            port=settings.DB_PORT
        )

    def execute(self, sql, params=None, many=True):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchall() if many else cursor.fetchone()

        cursor.close()
        conn.close()

        return result

    def commit(self, sql, params=None):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return result

    def execute_non_query(self, query, params=None):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        affected = cursor.rowcount
        cursor.close()
        conn.close()

        return affected