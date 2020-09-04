DROP DATABASE if EXISTS tableDB;
CREATE DATABASE tableDB;

USE tableDB;

DROP TABLE if EXISTS buytbl, usertbl;

CREATE TABLE usertbl
(userID CHAR(8) primary key,
NAME VARCHAR(10) NOT null,
birthYear INT not null,
addr CHAR(2) NOT null,
mobile1 CHAR(3) null,
mobile2 CHAR(8) null,
height SMALLINT null,
mDate DATE null
);




CREATE TABLE buytbl
(num INT auto_increment NOT NULL PRIMARY key,
userid CHAR(8) NOT null,
prodName CHAR(6) not null,
groupName CHAR(4) null,
price INT not null,
amount SMALLINT not NULL,
FOREIGN KEY(userid) REFERENCES usertbl(userID)
);

INSERT INTO userTBL VALUES
('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES
('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES
('KKH', '김경호', 1971, '젂남', '019', '3333333', 177, '2007-7-7');
INSERT INTO buyTBL VALUES(NULL, 'KBS', '운동화', NULL , 30, 2);
INSERT INTO buyTBL VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1); -- 외래키를 지정해서 아이디 없으면 안 들어감 오류
