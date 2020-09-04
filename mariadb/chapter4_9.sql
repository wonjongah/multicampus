USE sqldb;

SELECT * FROM testTbl4 
WHERE Fname = 'Mary';


delete FROM testtbl4 
WHERE Fname = 'Mary' LIMIT 5;  -- 다섯 개만 지우고 싶다!