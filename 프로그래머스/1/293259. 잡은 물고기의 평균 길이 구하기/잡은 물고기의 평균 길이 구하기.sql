-- 코드를 작성해주세요
SELECT ROUND(AVG(IFNULL(LENGTH, 10)), 2) AVERAGE_LENGTH
FROM FISH_INFO 


-- IFNULL 함수 --> LENGTH 값이 NULL 인 경우 10으로 대체 한다.
-- AVG 함수를 사용해 LENGTH 값들의 평균을 구한다.
-- ROUND 함수를 사용해 구한 LENGTH 평균 값을 소수점 2자리까지 출력한다.
