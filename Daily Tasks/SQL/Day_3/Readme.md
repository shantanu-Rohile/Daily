## 1. **NOT NULL Constraint.**

- NOT NULL Constraint will restrict the column from accepting null values

## 2. **UNIQUE Constraint.**

- UNIQUE Constraint will restrict the colum from accepting duplicate values and it can accept null value

## 3. **DEFAULT Constraint.**

- Default constraint is used so that when we INSERT Query is used but no value is given for certain column then default constraint will automaticaly a default value at that place.

## 4. **CHECK Constraint.**

- The CHECK constraint is used to ensure that the values in a column satisfies a specific condition.

## 5. **PRIMARY KEY Constraint.**

- Primary constraint restrict column in accepting only unique values, column with primary key constrain cannot empty.

## 6. **FOREIGN KEY Constraint.**

- Each Primary key of table represents the record of certain row.
- And when we want to connet 2 tables we use primary key of first table and foregin key i.e colum same as primary key of first table but in second table which is also not primary key of second table.

## 7. **what is select in sql**

- SELECT comes under DQL(Data Query Language)
- It is used to showcase the data

## 8. **what is where clause**

- WHERE caluse grant us abilty to filter
- Filter rows
- ```SELECT * FROM salesorder WHERE amount < 55000```

## 9. **what is having clause.**

- Having clause is used to filter groups

## 10. **what is the difference between where clause and having?**

# Difference Between WHERE and HAVING Clause
- 
| WHERE                                            | HAVING                                                                      |
| ------------------------------------------------ | --------------------------------------------------------------------------- |
| Filters individual rows                          | Filters groups                                                              |
| Used before `GROUP BY`                           | Used after `GROUP BY`                                                       |
| Used to filter records                           | Used to filter grouped records                                              |
| Generally used with normal conditions            | Commonly used with aggregate functions                                      |
| Cannot normally be used with aggregate functions | Can be used with aggregate functions like `COUNT()`, `SUM()`, `AVG()`, etc. |

