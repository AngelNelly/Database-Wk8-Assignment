--THIS IS THE ANSWER TO QUESTION 1. EVERY OTHER FILES HERE ARE ANSWERS TO QUESTION 2.


-- This SQL script creates a database for managing students and their course enrollments.
-- It includes the creation of tables for students, courses, and enrollments, along with some sample data.
-- The script assumes the use of MySQL or a compatible database system.
--This scripy is created by Angela Chinweike, a student of Power Learn Projectb Academy,  Software Engineering program.

--This creates the table for students identity and their information.
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);


--This creates the table for courses and their information.
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT
);


--This creates the table for enrollments, linking students to courses and including the enrollment date.
-- It also ensures that a student cannot enroll in the same course more than once.
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE(student_id, course_id) -- prevent duplicate enrollments
);


-- Sample data insertion for students, courses, and enrollments
INSERT INTO students (first_name, last_name, email) VALUES 
('Angela', 'Chinweike', 'angelachinweike@gmail.com'),
('Chinelo', 'Alloy', 'chineloalloy@gmail.com');
('Brenda', 'Fasie', 'brendafasie@gmail.com');
('Sisi', 'Mensa', 'sisimensa@gmail.com');
('Michael', 'Koors', 'michaelkoors@gmail.com');

-- Sample data for courses
INSERT INTO courses (course_name, description) VALUES 
('Math 101', 'Basic Mathematics'),
('Science 101', 'Basic Science');


-- Sample data for enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES 
(1, 1, '2025-05-04'),
(1, 2, '2025-05-04'),
(2, 1, '2025-05-04');


