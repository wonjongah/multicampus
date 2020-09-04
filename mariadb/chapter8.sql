USE tabledb;


CREATE VIEW v_userbuyTBL
AS
SELECT U.userid, U.name, B.prodname,
CONCAT(u.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
INNER JOIN buytbl B
ON U.userid = B.userID;

SELECT * FROM v_userbuytbl WHERE NAME = '김범수';  -- 컴럼명은 셀렉트 절에서 결정,  별칭 주고 싶으면as로 주면 된다