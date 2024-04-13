import psycopg2
from contextlib import contextmanager  # Імпортуємо декоратор contextmanager з модуля contextlib

@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        # Встановлюємо з'єднання з базою даних PostgreSQL
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="pass")
        yield conn  # Повертаємо з'єднання для використання в блоку with
        conn.close()  # Закриваємо з'єднання після завершення роботи з ним
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")  # Обробляємо помилку під час створення з'єднання з базою даних


def read_sql_file(filename)->str:
    with open(filename, "r") as f:
        result = f.read()
    return result

if __name__ == "__main__":
    print(read_sql_file('query_01.sql'))
