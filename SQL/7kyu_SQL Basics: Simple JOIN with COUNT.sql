-- Create your SELECT statement here
select
  p.id,
  p.name,
  count(t.name) as toy_count
from people p inner join toys t on p.id = t.people_id
group by p.id, p.name