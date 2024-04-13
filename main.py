import logging

from psycopg2 import sql, DatabaseError
from connect import create_connection, read_sql_file


if __name__ == "__main__":

    with create_connection() as conn:
        if conn is not None:
        # Створення курсора
        
            cur = conn.cursor()

            # Виконання 1 запиту
            query = read_sql_file('query_01.sql')
            # Знайти топ 5 студентів
            cur.execute(query)
            result = cur.fetchall()
            # Вивести результат
            print("Запит 1\nТоп 5 студентів з найвищим середнім балом:")
            for res in result:
                print(f"ID: {res[0]}, ПІБ: {res[1]}, Середній бал: {res[2]}")
            
            # Виконання 2 запиту
            query = read_sql_file('query_02.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 2\nСтудент із найвищим середнім балом з певного предмета")
            for res in result:
                print(f"ID: {res[0]}, ПІБ: {res[1]}, Середній бал: {res[2]} , Предмет: {res[3]}")

            # Виконання 3 запиту
            query = read_sql_file('query_03.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 3\nCередній бал у групах з певного предмета")
            for res in result:
                print(f"ID: {res[0]}, ПІБ: {res[1]}, Середній бал: {res[2]}, Предмет: {res[3]}")
            
            # Виконання 4 запиту
            query = read_sql_file('query_04.sql')
            cur.execute(query)
            result = cur.fetchone()
            print("\nЗапит 4\nСередній бал на потоці (по всій таблиці оцінок)")
            print(f"Середній бал: {result[0]}")

            # Виконання 5 запиту
            query = read_sql_file('query_05.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 5\nЯкі курси читає певний викладач")
            for res in result:
                print(f"ID: {res[0]}, ПІБ: {res[1]}, Предмет: {res[2]}")
            
            # Виконання 6 запиту
            query = read_sql_file('query_06.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 6\nСписок студентів у певній групі")
            for res in result:
                print(f"ID: {res[0]}, ПІБ: {res[1]}, Група: {res[2]}")


            try:
        # Збереження змін у базі даних
                conn.commit()
            except DatabaseError as e:
                logging.error(e)
                conn.rollback()
            finally:
        # Закриття курсора та з'єднання
                cur.close()
                conn.close()
        else:
            print("Error! cannot create the database connection.")