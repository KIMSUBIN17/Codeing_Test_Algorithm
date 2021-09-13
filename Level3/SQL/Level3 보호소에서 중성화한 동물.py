/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59045 */

SELECT *
FROM (
    SELECT ANIMAL_INS.ANIMAL_ID,	ANIMAL_INS.ANIMAL_TYPE,	ANIMAL_INS.NAME
    FROM ANIMAL_INS LEFT  OUTER JOIN ANIMAL_OUTS
    ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
    WHERE ANIMAL_INS.SEX_UPON_INTAKE LIKE '%Intact%'
    AND (ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE '%Neutered%'
    	OR ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE '%Spayed%')
    )
ORDER BY ANIMAL_ID