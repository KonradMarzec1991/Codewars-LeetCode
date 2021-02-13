-- Write your query here
CREATE EXTENSION pg_trgm;

CREATE INDEX full_name_idx ON prospects
USING gin (full_name gin_trgm_ops);

SELECT
  c.first_name,
  c.last_name,
  c.credit_limit AS old_limit,
  MAX(p.credit_limit) AS new_limit
FROM customers c, prospects p
WHERE p.full_name ILIKE '%' || c.first_name || '%'
AND p.full_name ILIKE '%' || c.last_name || '%'
AND p.credit_limit > c.credit_limit
GROUP BY 1, 2, 3
ORDER BY 1