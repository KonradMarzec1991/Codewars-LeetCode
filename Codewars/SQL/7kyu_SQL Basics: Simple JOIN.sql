-- Create your SELECT statement here
select
       p.*,
       c.name as company_name
from products p
join companies c on p.company_id = c.id;