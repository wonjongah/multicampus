SELECT company FROM productTBL;

SELECT * FROM membertbl;

SELECT memberName, memberAddress  -- 읽을 컬럼명 목록 
FROM membertbl;		-- 테이블 이름

SELECT *  -- 모든 컬럼 다 보겠다
FROM membertbl 
WHERE memberName = '지운이';  -- 조건절, 이 조건을 만족하는 행만 읽고 싶다
 -- =는 같냐라는 비교연산자, 데베에는 == 없음

CREATE TABLE `my tstTBL`(id INT);

DROP TABLE `my tstTBL`;