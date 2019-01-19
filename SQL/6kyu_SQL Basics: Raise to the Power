select t.id,t.heads, b.legs,t.arms,b.tails,
case
 when t.heads > t.arms then 'BEAST'
 when b.legs < b.tails then 'BEAST'
 when t.heads > t.arms and b.legs < b.tails then 'BEAST'
 else 'WEIRDO'
end as species
from top_half t
join bottom_half b on t.id = b.id
order by species;