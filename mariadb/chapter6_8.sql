USE employees;

SELECT E.first_name, E.last_name, DP.dept_name, D.from_date, D.to_date
FROM employees E
INNER JOIN dept_emp D
ON E.emp_no = D.emp_no
INNER JOIN departments DP
ON D.dept_no = DP.dept_no
WHERE D.to_date = '9999-01-01'  -- 직원들의 현재 부서가 어디냐!
ORDER by E.first_name, E.last_name;

