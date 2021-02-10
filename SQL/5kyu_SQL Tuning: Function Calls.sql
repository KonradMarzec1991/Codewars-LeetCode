WITH salary_inc AS (
  SELECT *, pctIncrease(department_id) AS ratio
  FROM departments
)

SELECT e.employee_id,
       e.first_name,
       e.last_name,
       s.department_name,
       e.salary AS old_salary,
       e.salary * (1 + s.ratio) AS new_salary
FROM employees e INNER JOIN salary_inc s USING (department_id)
ORDER BY 1;