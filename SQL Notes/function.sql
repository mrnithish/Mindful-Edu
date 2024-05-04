use farmers_set;
select ascii('5');
select char_length('Good Job');
show tables;
select concat(customer_first_name, ' ',customer_last_name) as Full_Name from customer;
select concat_ws('_',customer_first_name,customer_last_name) as Full_Name from customer;
select lcase(customer_first_name) from customer;
select lower(customer_first_name) from customer;
select ucase(customer_first_name) from customer;
select upper(customer_first_name) from customer;
select repeat('hi  ',5);
select replace('hi hello','hi','jjj');
select reverse('asdfgha');
select least(original_price,quantity)
from vendor_inventory;
select ln(2);
select log10(10);
select power(9,2);
