/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59045 */

        
        
/*1번 풀이 - 서브쿼리 사용
SELECT *
FROM (
    SELECT I.ANIMAL_ID,	I.ANIMAL_TYPE,	I.NAME
    FROM ANIMAL_INS I LEFT OUTER JOIN ANIMAL_OUTS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
    WHERE I.SEX_UPON_INTAKE LIKE 'Intact%'
    AND (O.SEX_UPON_OUTCOME LIKE 'Neutered%'
    	OR O.SEX_UPON_OUTCOME LIKE 'Spayed%')
    )
ORDER BY ANIMAL_ID


*/



/*
2번 풀이 - 구간 나누어 생각
ANIAML_INS A 기준/ ANIMAL_OUTS B 
들어올 때 : 중성화X = Intact
나갈 때 : 중성화O = Spayed / Neutered 
--> 'not' Intact라고 쉽게 생각
*/

SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A LEFT OUTER JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE 'Intact%' and B.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
ORDER BY A.ANIMAL_ID        
        
        
 /*3번 풀이*/       
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



