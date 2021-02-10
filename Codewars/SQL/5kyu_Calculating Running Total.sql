WITH current AS (
  SELECT
    DATE(created_at) as date,
    COUNT(*) AS count
  FROM posts
  GROUP BY 1
  ORDER BY 1
)


SELECT
  *,
  CAST(
      SUM(count) OVER (
          ROWS BETWEEN UNBOUNDED PRECEDING AND 0 FOLLOWING
      ) AS integer)
  AS total
FROM current;