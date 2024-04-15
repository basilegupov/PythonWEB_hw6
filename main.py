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
                print(f"ID: {res[0]}, Студент: {res[1]}, Середній бал: {res[2]}")
            
            # Виконання 2 запиту
            query = read_sql_file('query_02.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 2\nСтудент із найвищим середнім балом з певного предмета")
            for res in result:
                print(f"ID: {res[0]}, Студент: {res[1]}, Середній бал: {res[2]} , Предмет: {res[3]}")

            # Виконання 3 запиту
            query = read_sql_file('query_03.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 3\nCередній бал у групах з певного предмета")
            for res in result:
                print(f"ID: {res[0]}, Група: {res[1]}, Середній бал: {res[2]}, Предмет: {res[3]}")
            
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
                print(f"ID: {res[0]}, Викладач: {res[1]}, Предмет: {res[2]}")
            
            # Виконання 6 запиту
            query = read_sql_file('query_06.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 6\nСписок студентів у певній групі")
            for res in result:
                print(f"ID: {res[0]}, Студент: {res[1]}, Група: {res[2]}")

            # оцінки студентів у окремій групі з певного предмета
            query = read_sql_file('query_07.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 7\nОцінки студентів у окремій групі з певного предмета:")
            for res in result:
                print(f"Предмет: {res[0]}, Група: {res[1]}, Студент: {res[2]}, Оцінка: {res[3]}")
        
            # середній бал, який ставить певний викладач зі своїх предметів
            query = read_sql_file('query_08.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 8\nСередній бал, який ставить певний викладач зі своїх предметів:")
            for res in result:
                print(f"Викладач: {res[0]}, Предмет: {res[1]}, Оцінка: {res[2]}")
            
            # список курсів, які відвідує студент
            query = read_sql_file('query_09.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 9\nСписок курсів, які відвідує студент:")
            for res in result:
                print(f"Студент: {res[0]}, Предмет: {res[1]}")

            # Список курсів, які певному студенту читає певний викладач
            # query = read_sql_file('query_10.sql')
            # print(query)
            name_student = 'Тетяна Забара'
            name_professor = 'Зорян Базилевський'
            query = """
            SELECT Students.name AS student_name, Subjects.subject_name, Professors.name
            FROM Students
            JOIN Grades ON Students.id = Grades.student_id
            JOIN Subjects ON Grades.subject_id = Subjects.id
            JOIN Professors ON Subjects.professor_id = Professors.id
            WHERE Students.name = %s AND Professors.name = %s
            GROUP BY Students.name, Subjects.subject_name, Professors.name
            ORDER BY 1
            ; """
            cur.execute(query,(name_student, name_professor))
            result = cur.fetchall()
            print("\nЗапит 10\nСписок курсів, які певному студенту читає певний викладач")
            for res in result:
                print(f"Студент: {res[0]}, Предмет: {res[1]}, Викладач: {res[2]}")

            # Середній бал, який певний викладач ставить певному студентові
            query = read_sql_file('query_11.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 11\nСередній бал, який певний викладач ставить певному студентові:")
            for res in result:
                print(f"Викладач: {res[0]}, Студент: {res[1]}, Оцінка: {res[2]}")

            # Оцінки студентів у певній групі з певного предмета на останньому занятті
            query = read_sql_file('query_12.sql')
            cur.execute(query)
            result = cur.fetchall()
            print("\nЗапит 12\nОцінки студентів у певній групі з певного предмета на останньому занятті:")
            for res in result:
                print(f"Студент: {res[0]}, Предмет: {res[1]}, Оцінка: {res[2]}")

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