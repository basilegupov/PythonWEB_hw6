WITH LastGrades AS (
    SELECT student_id, subject_id, MAX(date_received) AS last_date_received
    FROM Grades
    GROUP BY student_id, subject_id
)
SELECT Students.name AS student_name, Subjects.subject_name, Grades.grade
FROM Students
JOIN LastGrades ON Students.id = LastGrades.student_id
JOIN Subjects ON LastGrades.subject_id = Subjects.id
JOIN Grades ON LastGrades.student_id = Grades.student_id AND LastGrades.subject_id = Grades.subject_id AND LastGrades.last_date_received = Grades.date_received
JOIN Groups ON Students.group_id = Groups.id
WHERE Groups.id = 2 AND Subjects.id = 3
