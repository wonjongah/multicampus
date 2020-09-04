USE sqldb;

SELECT A.emp AS '부하직원', B.emp AS '직속상관', B.empTel AS '직속상관연락처'
FROM emptbl A  -- 기준, 사원의!
INNER JOIN emptbl B  -- B.은 상사!
ON A.manager = B.emp
WHERE A.emp = '우대리';