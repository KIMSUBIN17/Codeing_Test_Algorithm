-- 코드를 입력하세요
SELECT TO_CHAR(SALES_DATE,'YYYY') AS YEAR
, TO_NUMBER(TO_CHAR(SALES_DATE, 'MM')) AS MONTH -- TO_CHAR --> 03, TO_NUMBER -> 3
, COUNT(DISTINCT(USER_ID)) AS PURCHASED_USERS
, ROUND(COUNT(DISTINCT(USER_ID)) / (SELECT COUNT(USER_ID) FROM USER_INFO WHERE TO_CHAR(JOINED,'YYYY') = '2021'), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID FROM USER_INFO WHERE TO_CHAR(JOINED,'YYYY') = '2021')
GROUP BY TO_CHAR(SALES_DATE,'YYYY'), TO_CHAR(SALES_DATE,'MM')
ORDER BY YEAR ASC, MONTH ASC







-- 신한카드 코딩테스트 유사문제 출제 
/*
#오답노트
- 비율구할때 같은 USER_ID가 여러 번 구매하는 경우도 있으므로 DISTICNT()를 사용해야 하는 것(☆☆☆)
- 2021년에 가입한 회원 찾기 --> 2021년에 가입한 사람의 USER_ID를 조회해 WHERE절 서브쿼리에서 ONLINE_SALE 테이블의 USER_ID와 같은 ID를 조회함


*/
