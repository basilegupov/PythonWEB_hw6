-- query_1.sql: Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.name, AVG(g.grade) AS avg_grade
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
GROUP BY s.name
ORDER BY avg_grade DESC
LIMIT 5;

-- query_2.sql: Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.name, AVG(g.grade) AS avg_grade
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_name = 'Mathematics'
GROUP BY s.name
ORDER BY avg_grade DESC
LIMIT 1;

-- query_3.sql: Знайти середній бал у групах з певного предмета.
SELECT g.group_name, AVG(grade) AS avg_grade
FROM Grades g
JOIN Students s ON g.student_id = s.student_id
JOIN Groups grp ON s.group_id = grp.group_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_name = 'Physics'
GROUP BY g.group_name;

-- query_4.sql: Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT AVG(grade) AS avg_grade FROM Grades;

-- query_5.sql: Знайти які курси читає певний викладач.
SELECT p.name AS professor_name, sub.subject_name
FROM Professors p
JOIN Subjects sub ON p.professor_id = sub.professor_id
ORDER BY p.name;

-- query_6.sql: Знайти список студентів у певній групі.
SELECT s.name AS student_name, grp.group_name
FROM Students s
JOIN Groups grp ON s.group_id = grp.group_id
WHERE grp.group_name = 'Group A';

-- query_7.sql: Знайти оцінки студентів у окремій групі з певного предмета.
SELECT s.name AS student_name, g.grade
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
JOIN Groups grp ON s.group_id = grp.group_id
WHERE sub.subject_name = 'Mathematics' AND grp.group_name = 'Group B';

-- query_8.sql: Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT p.name AS professor_name, AVG(g.grade) AS avg_grade
FROM Professors p
JOIN Subjects sub ON p.professor_id = sub.professor_id
JOIN Grades g ON sub.subject_id = g.subject_id
GROUP BY p.name;

-- query_9.sql: Знайти список курсів, які відвідує студент.
SELECT s.name AS student_name, sub.subject_name
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE s.name = 'John Doe';

-- query_10.sql: Список курсів, які певному студенту читає певний викладач.
SELECT s.name AS student_name, sub.subject_name
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
JOIN Professors p ON sub.professor_id = p.professor_id
WHERE s.name = 'John Doe' AND p.name = 'Professor X';

