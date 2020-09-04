USE sqldb;

CREATE TABLE testTBL2
(id INT AUTO_INCREMENT PRIMARY KEY,
userName CHAR(3),
age INT);

INSERT INTO testTBL2 VALUES(NULL, '지민', 25);  -- 속성 이름 작성 안 함, 생성했을 때 속성 순서대로
INSERT INTO testTBL2 VALUES(NULL, '유나', 22);
INSERT INTO testTBL2 VALUES(NULL, '유경', 21);

SELECT * FROM testTBL2;