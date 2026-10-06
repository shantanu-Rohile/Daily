
# Date : 05/10/2026

1. What is an Alias in SQL?

- a temporary name assigned to a table or a column within an SQL query

```SQL
SELECT AVG(Amount) as avg_amount from salesorder;
```

2. Scalar functions?

- A Scalar Function is a function that takes one or more inputs and return a single value but unlike aggrigate function where we take entire column as input scalar function works on single row value.

```SQL
SELECT LEN(std_name) from student where std_id = 101;

SELECT UPPER(std_name) from student;

SELECT ROUND(AVG(Amount),2) from salesorder;

SELECT NOW();
```

3. What is User-defined function? What are its various types?

- User defined function are the functions that are not not provided by SQL but are created by the user for specific purpose

- Scalar Functions

- Table-Valued Functions (TVFs)

4. oltp?

- Online Transaction Processing, is a type of database system that executes real time, concurrent trasactions such as INSERT, UPDATE, DELETE, with millisecond response time.  

5. olap?

-  (OLAP) is a technology that organizes large business databases to perform complex, multi-dimensional queries and trend analysis at high speeds.

6. What are the differences between OLTP and OLAP?

- OTLP
    - Used in daily trassactions
    - Data Source  : Current operationsal data
    - Storage type : row oriented
    - Response Time Mili-Seconds

- OLAP 
    - Analyze trends and historical data for decision-making.
    - Historical aggregated data.
    - Column-oriented
    - Seconds to minutes across large scans.

7. What is Collation?

- a set of rules that determines how character data (strings) is sorted and compared within a database

8. What is a Stored Procedure?

- a prepared batch of SQL statements grouped together into a single, reusable database object

9. What is a Recursive Stored Procedure?

-  in SQL. A recursive stored procedure is a procedure that calls itself directly or indirectly until it meets a specific boundary or termination condition

10. How to create empty tables with the same structure as another table?

```SQL
CREATE TABLE emp3 LIKE emp2;
```