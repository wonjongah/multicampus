
USE sqldb;

SELECT userID, SUM(amount)
FROM buytbl
GROUP BY userID;



SELECT userID, price*amount, price, amount  -- 가공 컬럼을 넣으면 새로운 컬럼이 하나 만들어짐
FROM buytbl
ORDER BY userID;

SELECT COUNT(userID) FROM buytbl;   -- 이 쿼리의 데이터 몇 개 있냐~

SELECT COUNT(*), COUNT(userID), COUNT(mobile1) FROM usertbl;   -- count 함수는 널 데이터를 세지 않는다
-- count(*) -> 널일 수도 있기 때문에 데이터 셀 때 자주 쓰는 표현

SELECT COUNT(*) FROM buytbl;