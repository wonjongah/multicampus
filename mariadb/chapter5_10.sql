SELECT CURRENT_USER(), DATABASE();

USE sqldb;
SELECT * FROM userTBL;
SELECT FOUND_ROWS();  -- 직전의 셀렉트로 행 몇 개 실행됐는지 리턴


UPDATE buyTBL SET price = price * 2;
SELECT ROW_COUNT();
