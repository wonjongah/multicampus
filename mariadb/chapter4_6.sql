USE sqlDB;

CREATE TABLE testTBL4 (id int, Fname varchar(50), Lname varchar(50));

-- 밑부터, 만들어진 테이블에 넣겠다
INSERT INTO testTBL4
SELECT emp_no, first_name, last_name
FROM employees.employees ;  -- 현재 데베 말고 다른 데베 접근하려면!!

CREATE TABLE testTBL5
(SELECT emp_no, first_name, last_name FROM employees.employees) ;  -- 테이블 생성!! 만들어진 테이블 없음