SELECT LPAD('이것이', 5, '##'), RPAD('이것이', 5, '##');

SELECT LTRIM('    이것이'), RTRIM('이것이    ');

SELECT TRIM('    이것이    '), TRIM(leading'ㅋ' FROM 'ㅋㅋㅋㅋ재밌어요.ㅋㅋㅋㅋ'); -- both, leading treailing

SELECT repeat('이것이', 3);

SELECT REPLACE('이것이 MariaDB다','이것이', 'This is');

SELECT REVERSE('MariaDB');