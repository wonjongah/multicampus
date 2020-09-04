USE sqldb;

SELECT height FROM userTbl WHERE addr = '경남';

SELECT NAME, height FROM userTbl WHERE height IN (SELECT height FROM userTbl WHERE addr = '경남');  -- some과 동일

SELECT NAME, mDate FROM userTbl order by mDate;

SELECT NAME, mDate FROM userTbl ORDER BY mDate DESC;

SELECT NAME, height FROM userTbl ORDER BY height DESC, NAME ASC;  -- 동률이 나왔을 땐~! 각자 제시해준다

SELECT addr FROM userTbl;

SELECT addr FROM userTbl ORDER BY addr;

SELECT DISTINCT addr FROM userTbl;