-- Replace with your SQL query
WITH grouped_month AS (
  SELECT
    DATE(date_trunc('month', created_at)) AS month,
    COUNT(title)::float as count
  FROM posts
  GROUP BY 1
  ORDER BY 1
),
lag_month AS (
  SELECT
  *,
  LAG(count, 1) OVER (ORDER BY month) AS previous_count
  FROM grouped_month
)


SELECT
  month AS date,
  count::integer,
  to_char(
    100 * (count - previous_count) / previous_count,
    'FM9990.0%'
  ) AS percent_growth
FROM lag_month;