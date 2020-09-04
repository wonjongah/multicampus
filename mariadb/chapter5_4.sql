SELECT 
ELT(2, '하나', '둘', '셋'),
FIELD('둘', '하나', '둘', '셋'),
FIND_IN_SET('둘', '하나,둘,셋'),
INSTR('하나둘셋', '둘'),
LOCATE('둘', '하나둘셋');


SELECT FORMAT(123456.123456, 4);

SELECT BIN(31), HEX(31), OCT(31);

SELECT INSERT('abcdefghi', 3, 4, '@@@@'), INSERT('abcdefghi', 3, 2, '@@@@');

SELECT LEFT('abcdefghi', 3), RIGHT('abcdefghi', 3);

SELECT LOWER('abcDFEFD'), UPPER('acbDDDDD');