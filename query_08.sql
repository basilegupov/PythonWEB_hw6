SELECT Professors.name AS professor_name, AVG(Grades.grade) AS avg_grade
FROM Professors
JOIN Subjects ON Professors.professor_id = Subjects.professor_id
JOIN Grades ON Subjects.subject_id = Grades.subject_id
GROUP BY Professors.name;

