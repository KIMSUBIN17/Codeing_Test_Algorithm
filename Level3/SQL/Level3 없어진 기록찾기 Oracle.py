/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59042 */

SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_OUTS B LEFT OUTER JOIN ANIMAL_INS A
ON B.ANIMAL_ID = A.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
ORDER BY B.ANIMAL_ID;
'''
LEFT OUTER JOIN 사용
입양간기록(ANIMAL_OUTS) 있는데, 들어온 기록(ANIMAL_INS)는 없는 상태

입양 간 기록은 존재하므로 ANIMAL_OUTS 데이터는 무조건 나와야함
->JOIN문 왼쪽에 ANIMAL_OUTS 테이블이 와야함
ANIMAL_OUTS와 ANIMAL_INS를 ANIMAL_ID가 같은 것을 기준으로 LEFT JOIN수행
->ANIMAL_OUTS테이블에 존재하는 ID와 그 ID와 같은 ANIMAL_INS테이블데이터가 연결됨
->ID값이 ANIMAL_INS테이블에 없다면? NULL값으로 연결
->WHERE조건으로 ANIMAL_INS자료가 NULL값인 것 찾음
'''