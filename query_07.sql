SELECT Students.name AS student_name, Grades.grade
FROM Students
JOIN Grades ON Students.student_id = Grades.student_id
JOIN Groups ON Students.group_id = Groups.group_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
WHERE Groups.group_name = 'Group B' AND Subjects.subject_name = 'Mathematics';

