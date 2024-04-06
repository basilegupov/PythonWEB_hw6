SELECT Students.name AS student_name, Subjects.subject_name
FROM Students
JOIN Grades ON Students.student_id = Grades.student_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
WHERE Students.name = 'John Doe';

