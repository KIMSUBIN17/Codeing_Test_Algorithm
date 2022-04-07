/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59045 */

SELECT *
FROM (
    SELECT ANIMAL_INS.ANIMAL_ID,	ANIMAL_INS.ANIMAL_TYPE,	ANIMAL_INS.NAME
    FROM ANIMAL_INS LEFT  OUTER JOIN ANIMAL_OUTS
    ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
    WHERE ANIMAL_INS.SEX_UPON_INTAKE LIKE 'Intact%'
    AND (ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%'
    	OR ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%')
    )
ORDER BY ANIMAL_ID


'''
참고링크 : https://blue-boy.tistory.com/196?category=743648



키 값으로 INNER JOIN을 한 뒤 ANIMAL_INS에서는 Intact로 시작하는 단어,
ANIMAL_OUTS에서는 Neutered나 Spayed로 시작하는 단어를 찾음
'''



