USE sqldb;

SELECT *
FROM buytbl
INNER JOIN usertbl
ON buytbl.userID = usertbl.userID
WHERE buytbl.userID = 'BBK';

SELECT buytbl.userID, NAME , prodName, addr, CONCAT(mobile1, mobile2) AS '연락처'
FROM buytbl
INNER JOIN usertbl
ON buytbl.userID = usertbl.userID
ORDER BY userTBL.name;

SELECT B.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM buytbl B
INNER JOIN usertbl U
ON B.userID = U.userID
WHERE B.userID = 'JYP'
ORDER BY U.userID;

SELECT U.addr, SUM(B.amount) AS '지역별 배송 수량',sum(B.price * B.amount) AS '지역별 매출 현황'
FROM usertbl U
INNER JOIN buytbl B
ON B.userID = U.userID
GROUP BY U.addr
ORDER BY U.addr;