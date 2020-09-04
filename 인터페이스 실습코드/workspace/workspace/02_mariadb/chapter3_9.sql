USE sqldb;

SELECT num, groupname, sum(price * amount) AS '비용'
FROM buytbl
GROUP BY groupName, num
WITH ROLLUP;

SELECT num, groupname, sum(price * amount) AS '비용'
FROM buytbl
GROUP BY groupName
WITH ROLLUP;