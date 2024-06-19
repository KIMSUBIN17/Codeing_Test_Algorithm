-- 코드를 작성해주세요
SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
-- 10진수를 2진수로 변환
WHERE CONV(GENOTYPE,10,2) NOT LIKE '%1_' AND    -- 2번형질이 없는 경우
(CONV(GENOTYPE, 10,2) LIKE '%1' OR      -- 1번형질이 있거나
CONV(GENOTYPE, 10, 2) LIKE '%1__')         -- 3번 형질이 있는 경우


/*
CONV() : 특정 숫자를 다른 숫자로 변환
*/