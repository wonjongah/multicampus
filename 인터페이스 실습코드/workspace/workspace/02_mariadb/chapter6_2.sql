USE sqlDB;
CREATE TABLE stdTBL(
stdName VARCHAR(10) NOT NULL PRIMARY KEY,
addr CHAR(4) NOT NULL
);
CREATE TABLE clubTBL(
clubName VARCHAR(10) NOT NULL PRIMARY KEY,
roomNo CHAR(4) NOT NULL
);
CREATE TABLE stdclubTBL(
num int AUTO_INCREMENT NOT NULL PRIMARY KEY,
stdName VARCHAR(10) NOT NULL,
clubName VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdTBL(stdName),
FOREIGN KEY(clubName) REFERENCES clubTBL(clubName)
);
INSERT INTO stdTBL VALUES
(N'김범수', N'경남'), (N'성시경', N'서울'), (N'조용필', N'경기'),
(N'은지원', N'경북'), (N'바비킴', N'서울');
INSERT INTO clubTBL VALUES
(N'수영', N'101호'), (N'바둑', N'102호'), (N'축구', N'103호'),
(N'봉사', N'104호');
INSERT INTO stdclubTBL VALUES
(NULL, N'김범수', N'바둑'), (NULL, N'김범수', N'축구'),
(NULL, N'조용필', N'축구'), (NULL, N'은지원', N'축구'),
(NULL, N'은지원', N'봉사'), (NULL, N'바비킴', N'봉사');