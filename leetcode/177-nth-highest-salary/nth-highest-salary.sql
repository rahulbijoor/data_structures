CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE salary_count INT;
  SELECT COUNT(DISTINCT salary) INTO salary_count FROM Employee;
  IF N > salary_count OR N <= 0 THEN
    RETURN NULL;
  END IF;
  RETURN (
      # Write your MySQL query statement below.
        SELECT nT.salary
        FROM (SELECT DISTINCT salary FROM  Employee ORDER BY salary DESC LIMIT N) AS nT
        ORDER BY nT.salary ASC
        LIMIT 1
  );
END