/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131120 */


SELECT MEMBER_ID, MEMBER_NAME, GENDER, TO_CHAR(DATE_OF_BIRTH,'YYYY-MM-DD') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER = 'W'  
AND TLNO IS NOT NULL
AND TO_CHAR(DATE_OF_BIRTH,'MM') = '03'
ORDER BY MEMBER_ID;


''
# 문제
MEMBER_PROFILE 테이블에서
생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성
이때 전화번호가 NULL인 경우는 출력대상에서 제외, 결과는 회원ID를 기준으로 오름차순 정렬

# 주의
DATE_OF_BIRTH의 데이트 포맷이 예시와 동일해야함

# 한번에 못푼 이유 😂
생일이 3월 => 부분 표현하기 위해 TO_CHAR와 'MM'을 한번에 생각해내지 못함
TO_CHAR(DATE_OF_BIRTH,'MM') = '03

TO_CHAR()에 대해 다시 살펴보기

- 문자형 -> 날짜형
TO_DATE('2017-05-12 23:59:59', 'YYYY-MM-DD HH24:MI:SS')


- 날짜형 -> 문자형
TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS')



'''
