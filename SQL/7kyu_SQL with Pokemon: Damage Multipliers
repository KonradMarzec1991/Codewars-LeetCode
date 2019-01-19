-- i choose you! --
select
  p.pokemon_name as pokemon_name,
  p.str * m.multiplier as modifiedStrength,
  m.element as element
from pokemon p join multipliers m on p.element_id = m.id
where p.str * m.multiplier >= 40
order by modifiedStrength desc;