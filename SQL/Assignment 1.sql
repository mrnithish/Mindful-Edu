use farmers_set;
show tables;
-- Table count
-- SELECT count(*) FROM INFORMATION_SCHEMA.TABLES
-- WHERE TABLE_SCHEMA = 'farmers_set';

-- ASSIGNMENT
-- 1 EXTRACT THE TOP 15 ROWS AND THE CUSTOMER_ID AND CUSTOMER_FIRST_NAME
select customer_id,customer_first_name from customer limit 15;

-- 2 EXTRACT THE TOP 15 ROWS WITH THE SAYE COLUMNS AND SKIP THE FIRST 2 ROWS
select customer_id,customer_first_name  from customer where customer_id between 3 and 15;

-- 3 SORT THE CUSTOMER TABLE BY CUSTOMER_NAYES
select * from customer order by customer_first_name;

-- 4 SORT THE CUSTOMERS TABLE BY DESCENDING ORDER RESPECT TO CUSTOMER_ID
select * from customer order by customer_first_name desc;

-- 5 EXTRACT ALL THE DATA WHOSE CUSTOMER_ZIP IS 22801
select * from customer where customer_zip=22801;

-- 6 EXTRACT ALL THE DATA WHOSE ZIP CODE IS OTHER THAN 22801
select * from customer where customer_zip!=22801;

-- 7 SORT ALL THE DATA WHOSE CUSTOMER IDs IS GREATER THAN 10 AS WELL AS THE PINCODE IS 22801
select * from customer where customer_id>10 and customer_zip=22801 order by customer_id;

-- 8 WHAT WOULD BE THE TOTAL NUMBER OF CUSTOMER_ID ??
select count( distinct customer_id) as Total from customer ;

-- 9 SORT OUT THE DATA TILL THE DATE 5th MAY 2019 ONLY WITH THE COLUMNS MARKET_DATE AND MARKET_START_TIME FROM THE TABLE
select market_date,market_start_time from market_date_info where market_date <= '2019-05-05' order by market_date;

-- 10 EXTRACT ALL THE PRODUCTS WHOSE PRODUCT SIZE IS MEDIUM AND LARGE
select * from product where product_size in ("medium","large");
