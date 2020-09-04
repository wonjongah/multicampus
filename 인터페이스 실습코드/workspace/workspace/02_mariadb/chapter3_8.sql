USE sqldb;

SELECT userID AS '사용자', SUM(price * amount) as '총구매액'
FROM buytbl
GROUP BY userID
HAVING SUM(price * amount) > 1000;

SELECT userID AS '사용자', SUM(price * amount) as '총구매액'
FROM buytbl
GROUP BY userID
HAVING SUM(price * amount) > 1000
ORDER BY SUM(price * amount);  -- 구매액이 적은 사용자부터 정렬
-- 그룹바이하면 그룹바이 컬럼, 집계함수로 쓰인 것을 오더바이로 쓸 수 있다

SELECT userID AS '사용자', SUM(price * amount) as '총구매액'
FROM buytbl
GROUP BY userID
HAVING SUM(price * amount) > 1000
ORDER BY 총구매액 DESC;  -- 수식 대신에 컬럼 명을 대신 써도 된다