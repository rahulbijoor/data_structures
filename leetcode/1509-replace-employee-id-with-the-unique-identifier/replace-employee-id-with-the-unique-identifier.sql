# Write your MySQL query statement below
SELECT t1.unique_id AS unique_id,t2.name 
FROM EmployeeUNI t1 RIGHT JOIN Employees t2 ON t1.id = t2.id;