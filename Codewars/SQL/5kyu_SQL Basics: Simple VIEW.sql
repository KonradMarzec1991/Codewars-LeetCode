-- Create your VIEW statement here
CREATE VIEW dep_aggs AS
SELECT
       s.department_id AS id,
       SUM(price)
FROM sales s
INNER JOIN departments d ON s.department_id = d.id
INNER JOIN products p ON s.product_id = p.id
GROUP BY s.department_id
HAVING SUM(price) > 10000;

CREATE VIEW members_approved_for_voucher AS
SELECT
       member_id AS id,
       m.name AS name,
       m.email AS email,
       SUM(price) as total_spending
FROM sales s
INNER JOIN members m ON s.member_id = m.id
INNER JOIN products p ON s.product_id = p.id
WHERE department_id IN (
    SELECT id FROM dep_aggs
)
GROUP BY member_id, m.name, email
HAVING SUM(price) > 1000;

SELECT
       id,
       name,
       email,
       total_spending
FROM members_approved_for_voucher
ORDER BY id;