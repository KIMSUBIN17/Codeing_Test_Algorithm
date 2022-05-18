/* 링크 : https://programmers.co.kr/learn/courses/30/lessons */
/*
ver.Oracle
*/

SELECT *
FROM PLACES A 
WHERE A.HOST_ID IN(
    SELECT HOST_ID
FROM PLACES B
GROUP BY HOST_ID
HAVING COUNT(*)>1)
ORDER BY ID
