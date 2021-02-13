SELECT
    date(created_at) AS day,
    description,
    COUNT(*)
FROM events
WHERE name = 'trained'
GROUP BY date(created_at), description
ORDER BY date(created_at), description;