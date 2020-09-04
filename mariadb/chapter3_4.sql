USE employees;

SELECT emp_no, hire_date FROM employees
ORDER BY hire_date ASC;

SELECT emp_no, hire_date FROM employees
ORDER BY hire_date ASC
LIMIT 5;

SELECT emp_no, hire_date FROM employees
ORDER BY hire_date ASC
LIMIT 10, 5;  -- limit 5 offset 0과 동일, 10번째부터 5개하면 10, 5

USE sqldb;


 DROP TABLE buyTbl2;
 
CREATE TABLE buyTbl2(SELECT * FROM buyTbl);
SELECT * FROM buyTbl2;

CREATE TABLE buyTbl4(SELECT USERID AS user, prodNAme AS product FROM buytbl);  --  as 생략 가능
SELECT * FROM buyTbl4;