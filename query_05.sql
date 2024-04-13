SELECT Professors.id, Professors.name AS professor_name, Subjects.subject_name
FROM Professors
JOIN Subjects ON Professors.id = Subjects.professor_id
WHERE Professors.id = 1;

