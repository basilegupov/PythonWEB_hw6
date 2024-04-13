SELECT Groups.id, Groups.group_name, AVG(Grades.grade) AS avg_grade, Subjects.subject_name
FROM Groups
JOIN Students ON Groups.id = Students.group_id
JOIN Grades ON Students.id = Grades.student_id
JOIN Subjects ON Grades.subject_id = Subjects.id
WHERE Subjects.subject_name = 'Physics'
GROUP BY Groups.id, Subjects.subject_name;

