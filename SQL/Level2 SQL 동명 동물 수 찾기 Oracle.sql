/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59041 */ 

SELECT NAME, COUNT(*) COUNT
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(*) >= 2
ORDER BY NAME