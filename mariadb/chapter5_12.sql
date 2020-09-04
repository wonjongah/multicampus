USE sqldb;

CREATE TABLE memberTBL LIKE usertbl; -- 구조만 복사!!!!

LOAD DATA LOCAL INFILE 'c:/temp/userTBL.txt' INTO TABLE membertbl;  -- 텍스트, 엑셀 데이터 가져와서 디비에 넣을 때

SELECT * FROM memberTBL;