/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59411 */

SELECT ANIMAL_ID, NAME
FROM 
(
    SELECT I.ANIMAL_ID, I.NAME, O.DATETIME - I.DATETIME AS 시간
    FROM ANIMAL_INS I INNER JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
    ORDER BY 시간 DESC
)
WHERE ROWNUM <=2;
'''
1. ANIMAL_IN과 ANIMAL_OUT 테이블을 ANIMAL_ID로 이너조인. 
2. 이 후 두 테이블의 DATETIME 컬럼의 차를 구함.
3. DATETIME컬럼의 차를 기준으로 내림차순 정렬
4. 내림차순 정렬한 위 테이블에서 상위 2개 출력(ROWNUM)

'''