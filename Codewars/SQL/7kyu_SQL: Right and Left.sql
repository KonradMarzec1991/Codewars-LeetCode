/*  SQL  */
select left(project, commits::int) as project,
right(address, contributors::int) as address
from repositories;