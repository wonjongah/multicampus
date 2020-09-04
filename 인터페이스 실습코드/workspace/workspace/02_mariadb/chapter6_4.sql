USE sqldb;

SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
LEFT OUTER JOIN buytbl B
ON U.userID = B.userID
ORDER BY U.userID;  -- 구매하지 않은 Null인 고객도 다 출력!!, 이너조인했을 때는 구매 안 한 고객은 나오지도 않았음

SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
right OUTER JOIN buytbl B -- inner join과 같은 결과, 구매한 고객만 나온다
ON U.userID = B.userID
ORDER BY U.userID;

SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
LEFT OUTER JOIN buytbl B
ON U.userID = B.userID
WHERE B.prodName IS NULL
ORDER BY U.userID; -- 구매이력 없는 사용자만 출력하라!

SELECT U.userID, U.name, IFNULL(SUM(B.price * B.amount), 0) AS '유저별 총 구매액'  -- 없으면 널 나오는 걸 보기 좋게 하고 싶다 널이면 0을 출력하고 싶음! isnull!! as는 밖에!!!!
FROM usertbl U
LEFT OUTER JOIN buytbl B
ON U.userID = B.userID
GROUP BY U.userID
ORDER BY U.userID;  -- 총 유저별로 (아우터조인) 총 합계, 총 -> 집계함수, 집계함수 쓰면 그룹바이