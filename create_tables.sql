drop table if exists Groups CASCADE;
CREATE TABLE Groups ( 
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL
);

drop table if exists Students CASCADE;
CREATE TABLE Students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    group_id INTEGER REFERENCES groups(id)
);

drop table if exists Professors CASCADE;
CREATE TABLE Professors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

drop table if exists Subjects CASCADE;
CREATE TABLE Subjects (
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL, 
    professor_id INT REFERENCES Professors(id)
);

drop table if exists Grades CASCADE;
CREATE TABLE Grades (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Students(id) ON DELETE CASCADE,
    subject_id INT REFERENCES Subjects(id) ON DELETE CASCADE,
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    date_received DATE NOT NULL
);
