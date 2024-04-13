SELECT Students.id, Students.name, AVG(Grades.grade) AS avg_grade
FROM Students
JOIN Grades ON Students.id = Grades.student_id
GROUP BY Students.id
ORDER BY avg_grade DESC
LIMIT 5;

