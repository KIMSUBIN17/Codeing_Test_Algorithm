-- 코드를 입력하세요
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY,PRICE) IN (SELECT CATEGORY, MAX(PRICE)
                         FROM FOOD_PRODUCT
                        GROUP BY CATEGORY
                        HAVING CATEGORY IN ('과자','국','김치', '식용유'))
ORDER BY PRICE DESC




/*
서브쿼리에 2개이상의 컬럼이 쓰여지는 경우 작성법
WHERE( COL1, COL2) IN (SELECT ~)
https://everyday-deeplearning.tistory.com/entry/ORACLE-MULTIPLE-COLUMN-SUBQUERY%EC%99%80-EXIST
*/
