SELECT Professors.name AS professor_name, Subjects.subject_name, AVG(Grades.grade) AS avg_grade
FROM Professors
JOIN Subjects ON Professors.id = Subjects.professor_id
JOIN Grades ON Subjects.id = Grades.subject_id
GROUP BY Professors.name, Subjects.subject_name;

