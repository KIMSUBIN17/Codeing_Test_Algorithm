/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/151136 */


SELECT ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'



'''
# 문제
CAR_RENTAL_COMPANY_CAR 테이블에서 
자동차 종류가 'SUV'인 자동차들의 평균 일일 대여 요금을 출력

# 주의사항
평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림하고, 컬럼명은 AVERAGE_FEE 로 지정



* ROUND함수
- 함수 : ROUND("값", "자리수)"
- 소수점 첫째자리 반올림
ROUND(AVG(DAILY_FEE),0) 에서 두번째 파라미터 0은 생략 가능



참고 링크 : https://gent.tistory.com/241

'''
