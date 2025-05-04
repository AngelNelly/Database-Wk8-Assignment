
-- This SQL script creates a database for managing students and their course enrollments.
-- It includes the creation of tables for students, courses, and enrollments, along with some sample data.
-- The script assumes the use of MySQL or a compatible database system.
--This scripy is created by Angela Chinweike, a student of Power Learn Projectb Academy,  Software Engineering program.


CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);


CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT
);


CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE(student_id, course_id) -- prevent duplicate enrollments
);


INSERT INTO students (first_name, last_name, email) VALUES 
('Angela', 'Chinweike', 'angelachinweike@gmail.com'),
('Chinelo', 'Alloy', 'chineloalloy@gmail.com');
('Brenda', 'Fasie', 'brendafasie@gmail.com');
('Sisi', 'Mensa', 'sisimensa@gmail.com');
('Michael', 'Koors', 'michaelkoors@gmail.com');

INSERT INTO courses (course_name, description) VALUES 
('Math 101', 'Basic Mathematics'),
('Science 101', 'Basic Science');

INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES 
(1, 1, '2025-05-04'),
(1, 2, '2025-05-04'),
(2, 1, '2025-05-04');
