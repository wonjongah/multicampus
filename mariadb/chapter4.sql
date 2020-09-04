USE sqldb;

CREATE TABLE testTBL1(id int, userName CHAR(3), age INT);

INSERT INTO testTBL1 VALUES(1, '홍길동', 25);
INSERT INTO testTBL1(id, userName) VALUES (2, '설현');
INSERT INTO testTBL1(userName, age, id) VALUES ('초아', 26, 3);

