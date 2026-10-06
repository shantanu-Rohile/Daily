## 1. **What are Tables and Fields?**

- Tables are stucture (rows and colummn) that holds records which is information we want to store.

- And fields are the the columns that stores the specific information

## 2. **What is a Join? List its different types.**

- JOIN in MySQL are used to combine the data from one or more columns based on related column

    - Types :
        - LEFT JOIN
        - RIGHT JOIN
        - INNER JOIN
        - FULL JOIN
        - SELF JOIN
        - CROSS JOIN
        - NATURAL JOIN

## 3. **What is a Self-Join?**

- self join is reffred join when when table is connected to itself with common column

## 4. **What is a Cross-Join?**

- CROSS JOIN Combines every row from first table with every row from second table

## 5. **What is the difference between Clustered and Non-clustered index?**

- A clustered index physically reorders and stores a table's data rows based on the index key, while a non-clustered index maintains a separate structure with pointers back to the original data rows.

## 6. **What is a Subquery? What are its types?**

- A subquery (also known as an inner query or nested query) is an SQL query embedded inside another SQL statement, such as a SELECT, INSERT, UPDATE, or DELETE statement. 

- The query containing the subquery is called the outer query or main query.

## 7. **What are some common clauses used with SELECT query in SQL?**

1. SELECT   - Specifies the columns or data fields to retrieve from the database.
2. FROM     - Identifies the source table or tables containing the desired data.
3. JOIN     - Merges rows from multiple tables based on a matching column relationship.
4. WHERE    - Filters individual rows out of the dataset using specified conditions.
5. GROUP BY - Aggregates duplicate row values into distinct summary buckets.
6. HAVING   - Filters grouped records by evaluating conditions on aggregate values.
7. ORDER BY - Sorts the final output rows in ascending or descending sequence.
8. LIMIT    - Controls the maximum total number of rows returned in the result.

## 8. **What are UNION, MINUS and INTERSECT commands?**

1. UNION     - Combines the unique rows from two or more SELECT query results. 
               Duplicates are automatically removed. 
               (Use UNION ALL to keep all duplicate rows).

2. INTERSECT - Returns only the distinct rows that are present in BOTH query results.
               It finds the common overlap between two datasets.

3. MINUS     - Returns distinct rows from the first query that DO NOT exist 
               in the second query. (Called EXCEPT in some SQL systems like 
               PostgreSQL and SQL Server).

## 9. **What is Cursor? How to use a Cursor?**

- A Cursor is a temporary database work area used to retrieve and manipulate data 
row-by-row. While standard SQL queries operate on an entire result set at once 
(set-based), a cursor acts as a pointer that loops through rows individually.

### HOW TO USE A CURSOR (4-Step Lifecycle)

1. DECLARE - Defines the cursor name and maps it to a specific SELECT query.
2. OPEN    - Executes the query, populates the cursor, and allocates memory.
3. FETCH   - Retrieves the current row data into variables and moves the 
             pointer to the next row. (Typically placed inside a loop).
4. CLOSE   - Releases the current data lock and frees the allocated memory.

## 10. **What are Entities and Relationships?**

### ENTITIES

An Entity is a distinct, real-world object, concept, or event that exists 
independently and stores data in a database. In a database schema, an entity 
translates directly into a Table.

* Key Trait: Represented by rows (records) and described by columns (attributes).
* Examples : "Customer", "Product", "Employee", "Order".


### RELATIONSHIPS

A Relationship is a logical association or link between two or more entities. 
In a relational database, relationships are established using Primary Keys 
and Foreign Keys.

* Key Trait: They define how data in one table connects to data in another.
* Examples : A Customer "PLACES" an Order; an Employee "WORKS_IN" a Department.


### THE 3 CARDINALITY TYPES

1. One-to-One (1:1)   - A row in Table A links to exactly one row in Table B.
                        (e.g., User -> UserProfile)
2. One-to-Many (1:M)  - A row in Table A links to multiple rows in Table B.
                        (e.g., Customer -> Orders)
3. Many-to-Many (M:N) - Multiple rows in Table A link to multiple rows in Table B.
                        Requires a junction table to resolve.
                        (e.g., Students <-> Courses)
