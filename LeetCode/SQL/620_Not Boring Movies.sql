SELECT *
FROM cinema
WHERE Id % 2 > 0 AND description NOT LIKE '%boring%'
ORDER BY rating DESC;