USE sqldb;

SELECT userID, amount
FROM buytbl
order BY userID;

SELECT userID, SUM(amount)
FROM buytbl
GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수'
FROM buytbl
GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(price * amount) AS '총 구매액'
FROM buytbl
GROUP BY userID;