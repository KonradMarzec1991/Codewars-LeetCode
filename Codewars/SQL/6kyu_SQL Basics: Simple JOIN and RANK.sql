-- Create your SELECT statement here
select p.id, p.name ,count(s.sale) as sale_count,
rank() over(partition by p.id order by p.id) as sale_rank
from people p
join sales s on s.people_id = p.id
group by p.id;