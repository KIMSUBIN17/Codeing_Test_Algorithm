/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59410 */ 

SELECT ANIMAL_TYPE, NVL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID;

/* NULL관련 함수
NVL(값1, 값2) : 값1이 null 이면 값2, 아니면 값1
NVL2(mgr,1,0) : mgr이 not null 이면 1, null 이면 0
NULLIF(exp1, exp2) : exp1 == exp2 이면 null, 다르면 첫번째 값
COALESCE(null,null,'abc') : abc => NULL이 아닌 첫번째 값
*/