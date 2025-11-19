CREATE DATABASE IF NOT EXISTS payroll_management;
USE payroll_management;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    designation VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    status VARCHAR(20)
);

INSERT INTO employees (name, designation, department, salary, status) VALUES
('Aarav Patel', 'Manager', 'HR', 75000, 'Active'),
('Riya Sharma', 'Developer', 'IT', 55000, 'Active'),
('Kabir Mehta', 'Analyst', 'Finance', 48000, 'Active'),
('Isha Nair', 'HR Executive', 'HR', 42000, 'Active'),
('Arjun Das', 'Designer', 'Marketing', 45000, 'Active'),
('Diya Verma', 'Tester', 'IT', 38000, 'Active'),
('Vivaan Gupta', 'Developer', 'IT', 60000, 'Active'),
('Anaya Singh', 'Accountant', 'Finance', 46000, 'Inactive'),
('Aditya Kumar', 'Support', 'Customer Care', 35000, 'Active'),
('Kavya Rao', 'Developer', 'IT', 50000, 'Active');

SELECT * FROM employees;