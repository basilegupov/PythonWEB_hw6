SELECT Students.name AS student_name, Groups.group_name
FROM Students
JOIN Groups ON Students.group_id = Groups.group_id
WHERE Groups.group_name = 'Group A';

