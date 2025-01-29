# Write your MySQL query statement below
SELECT name, bonus
FROM Bonus b RIGHT JOIN Employee e ON b.empID = e.empID
WHERE bonus < 1000 or bonus is NULL;