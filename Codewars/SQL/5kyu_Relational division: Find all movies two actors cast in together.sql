select title from
(
select f.title from film f
join film_actor fa on fa.film_id = f.film_id
where fa.actor_id = 105
) as c
natural join
(
select f.title from film f
join film_actor fa on fa.film_id = f.film_id
where fa.actor_id = 122
) as s;