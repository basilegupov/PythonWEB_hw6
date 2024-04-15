SELECT Professors.name AS professor_name, Students.name AS student_name, AVG(Grades.grade) AS avg_grade
FROM Professors
JOIN Subjects ON Professors.id = Subjects.professor_id
JOIN Grades ON Subjects.id = Grades.subject_id
JOIN Students ON Grades.student_id = Students.id
GROUP BY Professors.name, Students.name
ORDER BY 1;
