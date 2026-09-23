create database Practice;

use Practice;

create table emp (name varchar(50),id int);

insert into emp(name, id) values('Alice Smith', 101),
('Bob Johnson', 102),
('Charlie Brown', 103),
('Diana Prince', 104),
('Evan Wright', 105);

SELECT * FROM emp WHERE id between 101 and 104;

SELECT name FROM emp WHERE id IN (101,102);