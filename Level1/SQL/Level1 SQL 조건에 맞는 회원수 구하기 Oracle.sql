/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131535 */

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE TO_CHAR(JOINED, 'YYYY') = '2021'
AND AGE BETWEEN 20 AND 29;





/*
2021년에 가입한 회원 뽑기 위해 DATE 타입(2021-10-05)이었던  JOINED 데이터를 YYYY만 뽑아내어 조건을 걸어줌
WHERE 조건 2개 적용
1. 2021년에 가입한 회원
2. 나이가 20세 이상 29세 이하

*/

