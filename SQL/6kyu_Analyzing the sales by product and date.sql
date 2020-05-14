SELECT p.name as product_name ,
split_part(s.date::text, '-', 1)::int as year,
split_part(s.date::text, '-', 2)::int as month,
split_part(s.date::text, '-', 3)::int as day,
sum(sd.count * p.price) as total
from products p
join sales_details sd on sd.product_id = p.id
join sales s on s.id = sd.sale_id
group by p.name, rollup(year, month, day)
order by p.name, year, month, day;