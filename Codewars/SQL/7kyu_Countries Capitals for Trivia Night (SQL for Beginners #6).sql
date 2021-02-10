-- Your solution here
select capital from countries
where left(country, 1) = 'E'
and left(continent,4) = 'Afri'
order by capital
limit 3;