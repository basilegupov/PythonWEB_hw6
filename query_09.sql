SELECT Students.name AS student_name, Subjects.subject_name
FROM Students
JOIN Grades ON Students.id = Grades.student_id
JOIN Subjects ON Grades.subject_id = Subjects.id
GROUP BY Students.name, Subjects.subject_name
ORDER BY Students.name
-- WHERE Students.name = 'John Doe';

