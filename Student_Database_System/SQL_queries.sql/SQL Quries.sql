CREATE DATABASE StudentDB;

USE StudentDB;

##Students Table 
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    gender VARCHAR(10),
    department VARCHAR(50),
    address VARCHAR(100),
    phone VARCHAR(15)
);

##Courses Table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    department VARCHAR(50)
);

##Grades Table
CREATE TABLE Grades (
    grade_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    marks INT,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
);

##Attendance Table
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    total_classes INT,
    attended_classes INT,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
);

##Insert Sample Data
INSERT INTO Students VALUES
(1,'Rahul','Male','Computer Science','Pune','9876543210'),
(2,'Neha','Female','Information Technology','Mumbai','9876541230'),
(3,'Amit','Male','Computer Science','Delhi','9876545678');

INSERT INTO Courses VALUES
(101,'Database Management','Computer Science'),
(102,'Data Structures','Computer Science'),
(103,'Operating Systems','Information Technology');

INSERT INTO Grades VALUES
(1,1,101,85),
(2,1,102,78),
(3,2,103,90),
(4,3,101,70);

INSERT INTO Attendance VALUES
(1,1,101,40,35),
(2,1,102,40,30),
(3,2,103,40,38),
(4,3,101,40,32);

##View Data
SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Grades;

##Track Attendance
SELECT student_id,
       course_id,
       attended_classes,
       total_classes
FROM Attendance;

##Calculate Average Grades
SELECT student_id,
       AVG(marks) AS Average_Marks
FROM Grades
GROUP BY student_id;








