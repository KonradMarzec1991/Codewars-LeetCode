SELECT Email
FROM (
    SELECT Email, COUNT(Email) AS value
    FROM Person
    GROUP BY Email
    HAVING value > 1
) AS temp;