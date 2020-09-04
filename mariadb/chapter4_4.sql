USE sqldb;

SELECT * 
FROM testtbl2
ORDER BY id DESC;  -- 최근에 삽입된 순서대로 정렬, 즉 auto incremenet가 큰 순서로 정렬!
-- 나중에 들어간 값이 점점 더 id 값이 커질테니!