/* Write your PL/SQL query statement below */
select d.name as Department,e.name as Employee, e.salary as Salary 
from Employee e Left Join Department d on e.departmentid = d.id
where (e.departmentId,e.salary) In(select departmentId,Max(salary) 
                                    from employee 
                                    group by departmentId)