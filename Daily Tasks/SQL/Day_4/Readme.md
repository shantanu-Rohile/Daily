# Date : 28/09/2026

# Day : 4

## 1. **what is instring**
- INSTR() is built infunction in SQL used to get teh index of starting letter of substring from the main string.

```SQL
SELECT INSTR('DOWNPLAY','FLAY');
```

```
5
```

## 2. **what is substring**

- SUBSTRING() is inbuilt function in sql which used in data parsing, data cleaning

```SQL
SELECT SUBSTRING("Fool that doesn't belong to this era",1,5);
```

```
Fool 
```

## 3. **what is distinct.**

- DISTINT is used as filter in sql to only show distint data in that column

```sql
USE games;
SELECT distinct game_name, purchase_price_INR from games_owned;
```

## 4. **what is concate.**

- CONCAT() is a in-built function in sql to concat the values of columns 

```SQL
SELECT CONCAT(game_name,'  -INR ',purchase_price_INR) FROM games_owned;
```

## 5. **what is in operator.**

- IN operator is used when you want to match the values in column from given list

```SQL
SELECT game_name FROM games_owned WHERE category in ('AAA');
```

## 6. **what is between operator.**

- BETWEEN operator is used to dictate the range

```SQL
SELECT game_name FROM games_owned WHERE purchase_price_INR BETWEEN 300 AND 500;
```

## 7. **what is NOR & AND operator.**

- AND means all condtions should be true
- OR means at least one condtions should be true so the final result will be true


```SQL
SELECT *
FROM games_owned
WHERE category = 'AAA'
AND purchase_price_INR < 500;
```

```SQL
SELECT *
FROM games_owned
WHERE category = 'AAA'
OR purchase_price_INR < 500;
```

## 8. **what is sum .**
- SUM oF THE CONTENT OF COLUMNS

```SQL
SELECT SUM(purchase_price_INR) FROM games_owned;
```
## 9  **what min and max.**
- MIN & MAX are used to find the lowest and highest values in the column

```SQL
SELECT MIN(purchase_price_INR) FROM games_owned;
SELECT max(purchase_price_INR) FROM games_owned;
```
## 10. **what is top.**

- We use top in SQL Server
- but in MySql we use LIMIT to get top records as per condition mentioned

```sql
SELECT * FROM games_owned ORDER BY real_price_INR desc limit 10;
```