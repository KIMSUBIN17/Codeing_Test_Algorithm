/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/132203 */ 

SELECT DR_NAME, DR_ID, MCDP_CD, TO_CHAR(HIRE_YMD, 'YYYY-MM-DD') AS HIREYMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC;                                        




'''
1. 진료과가 CS 이거나 GS 인 경우 출력위해 OR 를 사용하였으나 그대신 IN 연산자 사용가능
조건이 많을경우에는 IN 을 사용하는 것이 더 좋음

SELECT DR_NAME, DR_ID, MCDP_CD, TO_CHAR(HIRE_YMD, 'YYYY-MM-DD') AS HIREYMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC;            


2. 내림차순 정렬 DESC , 오름차순 정럴 ASC

'''
