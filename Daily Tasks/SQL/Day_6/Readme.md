## 1. **CREATE**

```SQL
CREATE TABLE employee (empid INT PRIMARY KEY,emp_name VARCHAR(100));
```

## 2. **ALTER**

```SQL
ALTER TABLE employee ADD COLUMN salary INT;
```

## 3. **DROP**

```SQL
DROP employee;
```

## 4. **TRUNCATE**
```SQL
TRUNCATE employee;
```
## 5. **INSERT**

```SQL
INSERT INTO employee VALUES(101,'Shantanu',1200000),(102,'Prasad',1200000);
```
## 6. **UPDATE**

```SQL
UPDATE employee set salary = salary + 100000 where empid = 102;
```

## 7. **DELETE**


```SQL
DELETE FROM employee WHERE empid = 102;
```

## 8. **Grant**

```SQL
GRANT SELECT ON jvmsql.games TO 'jvmuser'@'localhost';
```


## 9. **Revoke**


```SQL
REVOKE ALL PRIVILEGES ON jvmsql.games FROM 'jvmuser'@'localhost';
```
