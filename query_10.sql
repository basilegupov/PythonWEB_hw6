SELECT Students.name AS student_name, Subjects.subject_name, Professors.name
FROM Students
JOIN Grades ON Students.id = Grades.student_id
JOIN Subjects ON Grades.subject_id = Subjects.id
JOIN Professors ON Subjects.professor_id = Professors.id
WHERE Students.name = 'Тетяна Забара' AND Professors.name = 'Зорян Базилевський'
GROUP BY Students.name, Subjects.subject_name, Professors.name
ORDER BY 1
;

