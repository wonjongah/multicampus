USE employees;

-- 두 컬럼의 실행 소요 시간 비교
SELECT * FROM employees WHERE emp_no = 10838;  -- 기본키로 셀렉트!! 훨 빠름, 바이너리로,, 기본키 생성시 자동으로 인덱스 생성!

SELECT * FROM employees WHERE first_name = 'Deniz';