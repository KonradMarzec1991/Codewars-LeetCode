-- add your query here!
SELECT p.name,
COUNT(d.detail) FILTER (WHERE d.detail = 'good') AS good,
COUNT(d.detail) FILTER (WHERE d.detail = 'ok') AS ok,
COUNT(d.detail) FILTER (WHERE d.detail = 'bad') AS bad
FROM products p
INNER JOIN details d ON p.id = d.product_id
GROUP BY p.id, p.name
ORDER BY p.name;