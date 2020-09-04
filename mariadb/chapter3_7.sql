USE sqldb;

SELECT AVG(amount) AS '평균 구매 개수'
FROM buytbl;

SELECT userID, AVG(amount) AS '평균 구매 개수'
FROM buytbl
GROUP BY userID;

SELECT name, MAX(height), MIN(height) FROM usertbl;  -- 잘못.. 제일 키 큰 사람과 작은 사람 알고 싶은 것 같은디.. -> 서브쿼리 이용!

SELECT NAME, MAX(height), MIN(height)  -- 잘못
FROM usertbl
GROUP BY NAME;

SELECT NAME, height
FROM usertbl
WHERE height = (SELECT MAX(height) FROM usertbl)
OR height = (SELECT MIN(height) FROM usertbl);


SELECT COUNT(*) FROM usertbl;

SELECT COUNT(mobile1) AS '휴대폰이 있는 사용자'
FROM usertbl;