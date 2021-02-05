SELECT class
FROM (
    SELECT class, COUNT(DISTINCT student) as count
    FROM courses
    GROUP BY class
) x
WHERE count >= 5;