/* Write your PL/SQL query statement below */
select name as Customers
from Customers
where id not in (SELECT Customers.id
                FROM Customers, Orders
                where Customers.id=Orders.customerId)