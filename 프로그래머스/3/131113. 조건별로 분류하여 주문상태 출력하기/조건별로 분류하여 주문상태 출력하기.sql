-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, TO_CHAR(OUT_DATE,'YYYY-MM-DD'),
       CASE WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') <= '2022-05-01'  THEN '출고완료'
            WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') >  '2022-05-01'  THEN '출고대기'
       ELSE '출고미정'
       END AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID

/*
출력할 컬럼이름은 쌍따옴표로 입력해야함
CASE표현식 구조
select case when 조건1 then 출력1
            when 조건2 then 출력2
            ...
            when 조건N then 출력N
	        else 출력N+1
       end "출력할컬럼이름Z"
from 테이블이름;
*/
