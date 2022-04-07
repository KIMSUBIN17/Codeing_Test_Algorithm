/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59413 */

SELECT HOUR, COUNT(*) AS "COUNT"



'''


#풀이:TO_CHAR()와 서브쿼리 이용, DATE 자료형을 시간별로 추출하고 GROUP BY절 활용해 해결
1. TO_CHAR()이용해서 '시간'값만 뽑아 HOUR이라고 정함
2. where절에 between 09 and 19사용해 09:00~19:59까지의 데이터만 조회하도록함
3. GROUP BY 이용해 HOUR로 그룹화함

#형변환 함수
TO_CHAR(날짜 or 숫자, '원하는 형태') : 날짜or숫자를 문자로 형변환함.
문자는 2번째 인자에서 지정한 형태로 출력됨
TO_CHAR(DATETIME,'HH24') -> 하루를 24시간으로 표시
ex. TO_CHAR(SYSDATE,'YYYY') / TO_CHAR(SYSDATE,'HH12') -> 하루를 12시간으로 표시

TO_DATE(문자) : 날짜처럼 생겼지만 데이터형이 날짜가 아니라 문자인 데이터를 날짜 데이터형으로 바꿔줌





#다른 풀이
SELECT HOUR, COUNT(O.DATETIME) AS COUNT
FROM
(
    SELECT LEVEL-1 AS HOUR
    FROM DUAL 
    CONNECT BY LEVEL<=24
)A LEFT join ANIMAL_OUTS O
ON A.HOUR = to_char(O.DATETIME,'HH24')
GROUP BY HOUR
ORDER BY HOUR;


# 참고소스 + LEVEL함수 관련 내용
https://blue-boy.tistory.com/195


#문제
문제 설명
ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

NAME	TYPE	NULLABLE
ANIMAL_ID	VARCHAR(N)	FALSE
ANIMAL_TYPE	VARCHAR(N)	FALSE
DATETIME	DATETIME	FALSE
NAME	VARCHAR(N)	TRUE
SEX_UPON_OUTCOME	VARCHAR(N)	FALSE
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

예시
SQL문을 실행하면 다음과 같이 나와야 합니다.

HOUR	COUNT
0	0
1	0
2	0
3	0
4	0
5	0
6	0
7	3
8	1
9	1
10	2
11	13
12	10
13	14
14	9
15	7
16	10
17	12
18	16
19	2
20	0
21	0
22	0
23	0




'''
