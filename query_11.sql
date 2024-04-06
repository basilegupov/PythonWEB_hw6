SELECT Professors.name AS professor_name, Students.name AS student_name, AVG(Grades.grade) AS avg_grade
FROM Professors
JOIN Subjects ON Professors.professor_id = Subjects.professor_id
JOIN Grades ON Subjects.subject_id = Grades.subject_id
JOIN Students ON Grades.student_id = Students.student_id
GROUP BY Professors.name, Students.name;
