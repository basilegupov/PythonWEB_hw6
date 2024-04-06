from faker import Faker
import random
import psycopg2
from psycopg2 import sql

fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Створення курсора
cur = conn.cursor()

# Додавання студентів
for _ in range(30):
    cur.execute(sql.SQL("INSERT INTO Students (name) VALUES (%s)"), [fake.name()])

# Додавання груп
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cur.execute(sql.SQL("INSERT INTO Groups (group_name) VALUES (%s)"), [group])

# Додавання викладачів
for _ in range(3):
    cur.execute(sql.SQL("INSERT INTO Professors (name) VALUES (%s)"), [fake.name()])

# Додавання предметів
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']
for subject in subjects:
    cur.execute(sql.SQL("INSERT INTO Subjects (subject_name, professor_id) VALUES (%s, %s)"), [subject, random.randint(1, 3)])

# Додавання оцінок
for student_id in range(1, 31):
    for subject_id in range(1, 6):
        for _ in range(20):
            cur.execute(sql.SQL("INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)"),
                        [student_id, subject_id, random.uniform(60, 100), fake.date_between(start_date='-1y', end_date='today')])

# Збереження змін у базі даних
conn.commit()

# Закриття курсора та з'єднання
cur.close()
conn.close()
