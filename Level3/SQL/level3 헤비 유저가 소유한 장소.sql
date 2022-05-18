/* 링크 : https://programmers.co.kr/learn/courses/30/lessons */
/*
ver.Oracle
*/


SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2
)
ORDER BY ID


/*
참고 - 다른 추가 풀이

SELECT *
FROM PLACES A 
WHERE A.HOST_ID IN(
    SELECT HOST_ID
FROM PLACES B
GROUP BY HOST_ID
HAVING COUNT(*)>1)
ORDER BY ID



*/
