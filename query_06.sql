SELECT Students.id, Students.name AS student_name, Groups.group_name
FROM Students
JOIN Groups ON Students.group_id = Groups.id
WHERE Groups.group_name = 'Group A';

