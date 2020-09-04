USE employees;

SELECT *
FROM employees
WHERE MONTH(birth_date) = MONTH(NOW())  -- 이것만 쓰면 이번달 생일인 사람
AND DAY(birth_date) = DAY(NOW());  -- 오늘 생일인 사람


SELECT DATEDIFF('2022-01-01', NOW()), TIMEDIFF('23:23:59', '12:11:10');

SELECT DAYOFWEEK(CURDATE()), MONTHNAME(CURDATE()), DAYOFYEAR(CURDATE());  -- DAYOFWEEK -> 몇요일, monthname -> 월 이름, dayofyear -> 일년 중 며칠이 지났는지

