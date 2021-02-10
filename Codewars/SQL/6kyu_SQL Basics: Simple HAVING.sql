-- Create your SELECT statement here
select age, count(people.id) as total_people
from people
group by age
having count(people.id) >= 10;