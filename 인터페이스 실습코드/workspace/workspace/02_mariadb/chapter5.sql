USE sqldb;

SELECT AVG(amount) AS '평균 구매 개수' FROM buytbl;

SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl;

SELECT CONVERT(AVG(amount), SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl;


SELECT CAST('2022$12%12' as date);
select CAST('2022/12/12' AS DATE);
SELECT CAST('2022%12%12' AS DATE);
SELECT CAST('2022@12@12' AS DATE);