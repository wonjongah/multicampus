USE sqldb;

UPDATE testtbl4
SET Lname = '없음'
WHERE Fname = 'kyoichi';

SELECT * FROM testtbl4
WHERE Fname = 'kyoichi'

