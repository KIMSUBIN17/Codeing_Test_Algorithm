SELECT TO_CHAR(DATETIME,'HH24') AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE TO_CHAR(DATETIME,'HH24') BETWEEN 09 AND 19
GROUP BY TO_CHAR(DATETIME,'HH24')
ORDER BY TO_CHAR(DATETIME,'HH24')


'''
DATE 자료형을 시간별로 추출하고 GROUP BY절 활용해 해결
1. 자료형이 DATE인 DATETIME칼럼의 시간 추출하기 위해 to_char 이용
2. where절에 between 09 and 19사용해 09:00~19:59까지의 데이터만 조회하도록함
3. 시간을 기준으로 GROUP BY, ORDER BY 사용해 그룹화,정렬화진행
'''