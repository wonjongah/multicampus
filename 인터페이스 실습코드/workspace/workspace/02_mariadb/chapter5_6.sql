SELECT CONCAT('이것이', SPACE(10), 'MariaDB다');

SELECT SUBSTRING('대한민국만세', 3, 2);

SELECT 
SUBSTRING_INDEX('cafe.naver.com', '.', 2),
SUBSTRING_INDEX('cafe.naver.com', '.', -2);

