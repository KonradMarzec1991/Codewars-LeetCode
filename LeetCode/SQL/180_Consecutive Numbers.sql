# Write your MySQL query statement below
SELECT DISTINCT n1.num AS ConsecutiveNums
FROM Logs AS n1, Logs AS n2, Logs AS n3
WHERE n1.id = n2.id + 1
AND n2.id = n3.id + 1
AND n1.num = n2.num
AND n2.num = n3.num;