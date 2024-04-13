import logging
from faker import Faker
import random
import psycopg2
from psycopg2 import sql, DatabaseError
from connect import create_connection

fake = Faker('uk-UA')

# Підключення до бази даних
with create_connection() as conn:
    if conn is not None:
        # Створення курсора
        cur = conn.cursor()

        # Додавання груп
        groups = ['Group A', 'Group B', 'Group C']
        for group in groups:
            cur.execute(sql.SQL("INSERT INTO Groups (group_name) VALUES (%s)"), [group])
        # conn.commit()

        # Додавання викладачів
        for _ in range(3):
            cur.execute(sql.SQL("INSERT INTO Professors (name) VALUES (%s)"), [fake.name()])
        # conn.commit()
        # Додавання предметів
        subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']
        for subject in subjects:
            cur.execute(sql.SQL("INSERT INTO Subjects (subject_name, professor_id) VALUES (%s, %s)"), [subject, random.randint(1, 3)])
        # conn.commit()
        # Додавання студентів
        for _ in range(30):
            cur.execute(sql.SQL("INSERT INTO Students (name, group_id) VALUES (%s, %s)"), [fake.name(), random.randint(1, 3)])
        # conn.commit()
        # Додавання оцінок
        for student_id in range(1, 31):
            for subject_id in range(1, 6):
                for _ in range(20):
                    cur.execute(sql.SQL("INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)"),
                                [student_id, subject_id, random.randint(0, 100), fake.date_this_decade()])
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


