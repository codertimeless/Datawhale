# TASK2

### 作业

- 超过5名学生的课（难度：简单）

```sql
SELECT class
FROM courses
GROUP BY class
HAVING count(DISTINCT student) >= 5;
```

- 交换工资(难度：简单)

```sql
UPDATE salary
SET sex=if(sex = "f","m","f");
```

- 有趣的电影（难度：简单）

```sql
SELECT id,movie,description,rating
FROM cinema
WHERE (description <> "boring") and (id%2=1)
ORDER BY rating DESC;
```

- 组合两张表(难度：简单)

```sql
SELECT FirstName,LastName,City,State
FROM Person LEFT JOIN Address
WHERE Person.PersonId=AddressId.PersonId;
```

- 删除重复的邮箱（难度：简单）

```sql
SELECT p1.*
FROM email p1,
    email p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id;
```

- 从不订购的客户（难度：简单）

```sql
SELECT Name as Customers
FROM Customers
WHERE Customers.Id NOT IN
(SELECT CustomerId
FROM orders);
```

- 超过经理收入的员工（难度：简单）

```sql
SELECT E.Name as Employee
FROM Employee E JOIN Employee S
WHERE (E.ManagerId = S.Id) and (E.Salary > S.Salary);
```

