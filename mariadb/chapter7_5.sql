USE tabledb;

ALTER TABLE usertbl
ADD homepage varchar(30)  -- 열추가
DEFAULT 'http://www.hanbit.co.kr'
NULL; -- 널허용


ALTER TABLE usertbl
DROP column mobile1;

ALTER TABLE usertbl
CHANGE COLUMN NAME uName VARCHAR(20) NULL;