# Write your MySQL query statement below
select m.name as Employee
from Employee s join Employee m on m.managerId=s.id
where m.salary>s.salary