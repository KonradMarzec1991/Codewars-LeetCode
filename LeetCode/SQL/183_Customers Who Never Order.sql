SELECT c.Name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.ID = o.CustomerId
WHERE o.CustomerId IS NULL;