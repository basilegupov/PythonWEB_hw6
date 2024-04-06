SELECT Professors.name AS professor_name, Subjects.subject_name
FROM Professors
JOIN Subjects ON Professors.professor_id = Subjects.professor_id;

