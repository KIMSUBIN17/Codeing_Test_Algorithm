/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59041 */ 
/* 문제 조건 : 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 
이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요. */

SELECT NAME, COUNT(NAME) AS 'COUNT'
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME


/*풀이 : 2번이상 쓰인 이름을 group by로 묶음
group by의 조건은 where절이 아니라 having절 사용*/