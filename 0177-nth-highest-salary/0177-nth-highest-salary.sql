CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select salary 
      from (select salary, rank() over(order by salary desc) as srank
            from employee
            group by salary) as a
      where srank = N
      limit 1
  );
END