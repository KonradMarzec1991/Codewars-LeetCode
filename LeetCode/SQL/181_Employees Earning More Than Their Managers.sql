SELECT e.Name AS Employee
FROM Employee e
LEFT JOIN Employee em ON e.ManagerId = em.Id
WHERE e.Salary > em.Salary;