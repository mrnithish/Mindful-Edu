-- SQL OPERATORS
USE students;
 
 CREATE TABLE stu_marklist
 (
 stu_id int ,
 stu_name varchar (30),
 Math int,
 Science int,
 Socialstudies int,
 Tamil int,
 English int
);

insert into stu_marklist
values (1201,'alex',70,50,88,92,60),
	   (1202,'bhavya',56,79,82,90,34),
       (1203,'cate',89,70,80,92,45),
       (1204,'dharshan',98,82,87,94,96),
       (1205,'esten',45,56,70,49,76);
       
TRUNCATE stu_marklist;
select * from stu_marklist;
-- THERE ARE MAJORLY 3 TYPES OF OPERATORS THEY ARE
 -- 1. ARITHMETIC
 -- 2. COMPARISON
 -- 3. LOGICAL OPERATORS
 
 -- 1. ARITHMETIC OPERATORS:
 
 -- I) + operator : adds 2 given values
 
 
 select Tamil + English as Lang_marks from stu_marklist;
 
 -- II) - operator : subtracts the given 2 values
 
 select Math - Science as diff from stu_marklist
 where stu_name = 'alex';
 
 -- III) * operator : multipiles the given 2 values
 
 select Science * Socialstudies as Product from stu_marklist
 where stu_name = 'cate';
 
 -- IV) / operator : divides the given values
 
 select Math - Socialstudies as qtn from stu_marklist;
 
 -- 2. COMPARISON OPERATORS :
 
 -- I) = EQUAL TO
 
 select * from stu_marklist;
 
 SELECT stu_name,
		stu_id,
        Math
from stu_marklist
where Math = 70;        
 
 -- II) != OR <> NOT EQUAL TO
 
 SELECT stu_name,
		stu_id,
        Tamil
from stu_marklist
where Tamil != 92; 

 --  III) > GREATER THAN
 
 select * 
 from stu_marklist
 where Socialstudies > 75;
 
 -- IV) >= GREATER THAN OR EQUAL TO
 
  select * 
 from stu_marklist
 where Socialstudies >= 85;
 
 -- V) < LESSER THAN 
 
select * 
from stu_marklist
where Tamil < 95;
 
-- VI) <= LESSER THAN OR EQUAL TO 

 select * 
 from stu_marklist
 where Tamil <= 50;
 
  -- 3. LOGICAL OPERATORS
  
  -- I) ALL : COMPARE ALL VALUES  FROM ONE TABLE TO ALL THE OTHER VALUES IN THE OTHER TABLE PROVIDED BOTH ARE INTHE SAME DATABASE.

SELECT *
FROM teach_info
where teach_age > ALL (
SELECT stu_age
FROM stu_info
);
select * from stu_info;
select * from teach_info; 

-- II) AND : RETURNS RECORDS IF ALL THE CONDITIONS OF AND IS TRUE

 select * from stu_marklist;
 
SELECT * 
FROM  stu_marklist
where Tamil = 88 AND English = 60;

-- III) OR : RETURNS RECORDS IF ANY OF THE CONDITION OF OR IS TRUE

SELECT * 
FROM  stu_marklist
where Tamil = 49 OR English = 56;

-- IV) BETWEEN : SHOWS THE RECORDS WITHIN THE MENTIONED RANGE.

SELECT * 
FROM stu_marklist
WHERE Math BETWEEN 40 AND 95;

-- V) IN : ALLOWS USERS TO SPECIFY TWO OR MORE VALUES IN THE WHERE CLAUSES

SELECT *
FROM stu_marklist
WHERE Socialstudies IN (88,70,80);

-- VI) NOT : RETURNS RECORDS IF THE CONDITION IS FALSE

SELECT *
FROM stu_marklist
WHERE  NOT Math = 45; 

-- VII) ANY : RETURNS RECORDS IF THIER IS A MATCH BY COMPARING THE VALUES IN ONE TABLE TO THE OTHER TABLE

SELECT *
FROM stu_info
where stu_age < ANY (
SELECT teach_age
FROM teach_info
);



 



