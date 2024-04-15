SELECT Subjects.subject_name, Groups.group_name, Students.name AS student_name, Grades.grade
FROM Students
JOIN Grades ON Students.id = Grades.student_id
JOIN Groups ON Students.group_id = Groups.id
JOIN Subjects ON Grades.subject_id = Subjects.id
WHERE Groups.group_name = 'Group B' AND Subjects.subject_name = 'Mathematics';

