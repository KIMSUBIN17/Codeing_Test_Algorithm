-- 코드를 입력하세요
SELECT TO_CHAR(OS.SALES_DATE,'YYYY') AS YEAR
,TO_NUMBER(TO_CHAR(OS.SALES_DATE,'MM')) AS MONTH
, UI.GENDER
, COUNT(DISTINCT OS.USER_ID) AS USERS
FROM USER_INFO UI
INNER JOIN ONLINE_SALE OS ON UI.USER_ID = OS.USER_ID
GROUP BY TO_CHAR(OS.SALES_DATE,'YYYY') ,TO_NUMBER(TO_CHAR(OS.SALES_DATE,'MM')),UI.GENDER
HAVING UI.GENDER IS NOT NULL
ORDER BY YEAR, MONTH, GENDER ASC



/* #오답노트
1. GROUP BY 절을 작성하지 않았을때 
ORA-00937: not a single-group group function 오류 발생
그룹함수를 사용하였는데 GROUP BY 절을 사용하지 않아 발생한 에러로, 
그룹함수를 사용하면 GROUP BY 절을 추가해야하며, GROUP BY 절에는 SELECT 절에 있는 모든 컬럼을 작성해야함
2. 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재
--> USERS 회원수 COUNT할 때 DISTINCT로 중복제거 
3. MONTH 값 구할 때 TO_CHAR만 하니 월 값이 01,02,03이런식으로 나와서 계속 오답처리됨
--> TO_CHAR 형변환값을 TO_NUMBER로 한번더 감싸서 1,2,3,4... 처럼 정수로만 표현되도록 함(정답!)
*/

