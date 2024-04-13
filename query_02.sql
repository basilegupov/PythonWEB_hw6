SELECT Students.id, Students.name, AVG(Grades.grade) AS avg_grade, Subjects.subject_name
FROM Students
JOIN Grades ON Students.id = Grades.student_id
JOIN Subjects ON Grades.subject_id = Subjects.id
WHERE Subjects.subject_name = 'Mathematics'
GROUP BY Students.id, Subjects.subject_name
ORDER BY avg_grade DESC
LIMIT 1;

