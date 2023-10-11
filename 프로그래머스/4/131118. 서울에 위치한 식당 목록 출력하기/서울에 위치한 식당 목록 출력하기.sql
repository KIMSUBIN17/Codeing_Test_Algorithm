-- 코드를 입력하세요
SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, B.SCORE
FROM REST_INFO A 
INNER JOIN (
    SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
    FROM REST_REVIEW
    GROUP BY REST_ID) B
ON A.REST_ID = B.REST_ID
WHERE A.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC


/* [오답노트]
서브쿼리 없이 다 SELECT에 담으니 오류 발생
ORA-00937: not a single-group group function
>> 집계함수를 사용했으므로 GROUP BY 절이 필요한데, SELECT 절에 사용된 내용이 모두 GROUP BY에 들어가야함 
--> REST_ID만으로 GROUP BY 하기 위해서는 서브쿼리를 사용해야함
*/