/* Write your PL/SQL query statement below */
SELECT customer_number
FROM (SELECT customer_number, rank() over(order by count(order_number) desc) as r
      FROM Orders
      GROUP BY customer_number)
WHERE r=1;