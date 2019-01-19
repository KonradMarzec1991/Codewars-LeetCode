-- Create your SELECT statement here
with special_sales as (
  select * from sales
  where price > 90.00
)

select * from departments where id in
(select department_id from sales where price > 90.00)