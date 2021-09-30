/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59412 */

SELECT HOUR, COUNT(*) AS "COUNT"
FROM
    (SELECT TO_CHAR(DATETIME,'HH24') AS HOUR
    FROM ANIMAL_OUTS)
WHERE HOUR BETWEEN 09 AND 19
GROUP BY HOUR
ORDER BY HOUR;


'''
#문제
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

#풀이:TO_CHAR()와 서브쿼리 이용, DATE 자료형을 시간별로 추출하고 GROUP BY절 활용해 해결
1. TO_CHAR()이용해서 '시간'값만 뽑아 HOUR이라고 정함
2. where절에 between 09 and 19사용해 09:00~19:59까지의 데이터만 조회하도록함
3. GROUP BY 이용해 HOUR로 그룹화함

#형변환 함수
TO_CHAR(날짜 or 숫자, '원하는 형태') : 날짜or숫자를 문자로 형변환함.
문자는 2번째 인자에서 지정한 형태로 출력됨
ex. TO_CHAR(SYSDATE,'YYYY') / TO_CHAR(SYSDATE,'HH12') -> 하루를 12시간으로 표시
TO_DATE(문자) : 날짜처럼 생겼지만 데이터형이 날짜가 아니라 문자인 데이터를 날짜 데이터형으로 바꿔줌



#다른 풀이
SELECT TO_CHAR(DATETIME,'HH24') AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE TO_CHAR(DATETIME,'HH24') BETWEEN 09 AND 19
GROUP BY TO_CHAR(DATETIME,'HH24')
ORDER BY TO_CHAR(DATETIME,'HH24')


'''