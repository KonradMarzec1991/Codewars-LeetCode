SELECT name, population, area
FROM World
WHERE area > 3000000 OR population > 25000000;

/*Other great solution from LeetCode*/
SELECT name, population, area
FROM world
WHERE area > 3000000
UNION
SELECT name, population, area
FROM world
WHERE population > 25000000;