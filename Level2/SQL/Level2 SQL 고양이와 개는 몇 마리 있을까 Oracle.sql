/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59040 */

SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS "count"
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;


#검색해보면 동물의 타입은 개, 고양이2종류임
#group by로 개와 고양이를 분리한 다음 각각 몇마리씩인지 확인
