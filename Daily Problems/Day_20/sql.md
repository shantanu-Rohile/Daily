1. What is SQL ?

    - SQL stands for structured query language which specially designed for communicating with the database.

    - I very popular language that is used in many database mangagment systems like MySQL, PSQL, Oracle

2. What is the use of IFNULL() function in Oracle?

    - IFNULL() is used to replace null values to real value.
    - ```IFNULL('age',18) FROM members;```

3. What is Unique Key?

    - Unique key is column that unique indefies the value. Thre can be multple unique keys in table.The Entry of null values are allowed in the unique keys. 

    ```SQL
    CREATE TABLE emp (empid INT UNIQUE,empname CHAR(100)); 
    ```

4. What is difference between Unique Key Constraint and Primary Key Constraint?

 - primary key :
    - Primary key is generally used in table to represent a record.
    - Null values are not allowed in primary key.
    - There can be only 1 primary key in column

- UNIQUE CONSTRAINT :
    - UNIQUE Constraint is used to remove duplicate values except null
    - NULL Values are allowed
    - There can be multiple unique columns in the table.


