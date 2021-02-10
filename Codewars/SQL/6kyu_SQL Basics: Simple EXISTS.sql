-- Create your SELECT statement here
select id, name
from departments
where exists
(select * from departments
inner join sales
on departments.id = sales.department_id
where sales.price > 98.00);