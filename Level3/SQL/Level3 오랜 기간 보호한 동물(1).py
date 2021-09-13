/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59044 */

SELECT *
FROM(
    SELECT A.NAME, A.DATETIME
    FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B
    ON A.ANIMAL_ID = B.ANIMAL_ID
    WHERE B.ANIMAL_ID IS NULL
    ORDER BY A.DATETIME
)
WHERE ROWNUM < 4;


'''
왼쪽 테이블 기준으로 LEFT JOIN 수행(왼쪽 테이블 전체 + 오른쪽 테이블에서 조건에 해당하는 부분만 조인)
ROWNUM과 인라인 뷰 사용해 DATETIME을 내림차순 정렬
ROWNUM <4 : ROWNUM이 4미만인 값 추출

'''
