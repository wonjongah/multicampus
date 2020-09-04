USE tabledb;

DROP TABLE if EXISTS prodTBL;

CREATE TABLE prodTBL
(
prodCode CHAR(3) NOT NULL,
prodID CHAR(4) NOT NULL,
prodDate DATETIME NOT NULL,
prodCur CHAR(10) NULL
);

ALTER TABLE prodTBL
ADD CONSTRAINT PRIMARY KEY(prodCode, prodID);  -- 복합키, 이 두 개의 조합이 유일해야 한다