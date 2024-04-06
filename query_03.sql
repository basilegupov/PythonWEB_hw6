SELECT Groups.group_name, AVG(Grades.grade) AS avg_grade
FROM Groups
JOIN Students ON Groups.group_id = Students.group_id
JOIN Grades ON Students.student_id = Grades.student_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
WHERE Subjects.subject_name = 'Physics'
GROUP BY Groups.group_name;

