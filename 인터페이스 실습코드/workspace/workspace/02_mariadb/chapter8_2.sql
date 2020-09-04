USE employees;

SELECT * FROM employees WHERE emp_no = 10838;

SELECT * FROM employees WHERE first_name = 'Deniz';

CREATE INDEX idx_employees_first_name
ON employees (first_name);

DROP INDEX idx_userTBL_name ON usertbl;
SHOW INDEX FROM usertbl;