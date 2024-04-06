CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(100)
);

CREATE TABLE Professors (
    professor_id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100),
    professor_id INT REFERENCES Professors(professor_id)
);

CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Students(student_id),
    subject_id INT REFERENCES Subjects(subject_id),
    grade FLOAT,
    date_received DATE
);
