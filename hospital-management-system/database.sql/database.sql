CREATE DATABASE hospital_db;

USE hospital_db;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(100)
);

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100),
    doctor_name VARCHAR(100),
    appointment_date DATE
);

CREATE TABLE billing (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100),
    treatment VARCHAR(100),
    amount INT
);









