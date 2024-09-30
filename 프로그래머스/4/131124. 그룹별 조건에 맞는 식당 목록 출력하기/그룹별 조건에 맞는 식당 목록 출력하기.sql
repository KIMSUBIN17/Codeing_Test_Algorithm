-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, TO_CHAR(REVIEW_DATE,'YYYY-MM-DD') AS  REVIEW_DATE
FROM MEMBER_PROFILE M INNER JOIN REST_REVIEW R
ON M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID IN (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     HAVING COUNT(*) = (
                     SELECT MAX(COUNT(*))
                     FROM REST_REVIEW
                    GROUP BY MEMBER_ID
                     )
                )
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC

/*
1. MEMBER_ID로 두 테이블 조인하고 WHERE 조건으로 리뷰수가 가장 많은 MEMBER_ID 찾음
2.하위 HAVING절에서 리뷰 수가 가장 많은 사람을 MAX로 뽑음
*/