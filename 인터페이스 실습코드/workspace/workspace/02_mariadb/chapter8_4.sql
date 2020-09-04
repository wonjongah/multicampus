GRANT ALL PRIVILEGES ON employees.* TO 'iot_user'@'%';  -- 불가, 루트만 할 수 있는 일

SELECT * FROM employees.employees;  -- 권한 없어서 사용불가