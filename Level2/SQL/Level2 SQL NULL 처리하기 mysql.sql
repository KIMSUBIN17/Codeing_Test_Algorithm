/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59410 */ 

SELECT ANIMAL_TYPE, IFNULL(NAME,'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID



'''
#문제
입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

#NULL관련 함수
NVL(값1, 값2) : 값1이 null 이면 값2, 아니면 값1
NVL2(mgr,1,0) : mgr이 not null 이면 1, null 이면 0
NULLIF(exp1, exp2) : exp1 == exp2 이면 null, 다르면 첫번째 값
COALESCE(null,null,'abc') : abc => NULL이 아닌 첫번째 값


'''