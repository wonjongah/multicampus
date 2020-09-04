USE employees;

SELECT first_name FROM employees;

SELECT first_name, last_name, gender FROM employees;

SELECT first_name AS 이름, gender AS 성별 FROM employees;  -- 별칠

SELECT first_name 이름, gender 성별, hire_date 입사일 FROM employees;

SELECT * 
FROM employees
WHERE last_name = 'Lenart';

SELECT *
FROM employees
WHERE birth_date >= '1960-01-01';

SELECT *
FROM employees
WHERE birth_date >= '1960-01-01'
AND birth_date <= '1960-12-31';

SELECT *
FROM employees
WHERE birth_date BETWEEN '1960-01-01' AND '1960-12-31';

SELECT *
FROM employees
WHERE last_name IN('lenart', 'Baaz', 'Pillow');