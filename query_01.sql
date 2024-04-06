SELECT Students.name, AVG(Grades.grade) AS avg_grade
FROM Students
JOIN Grades ON Students.student_id = Grades.student_id
GROUP BY Students.student_id
ORDER BY avg_grade DESC
LIMIT 5;

