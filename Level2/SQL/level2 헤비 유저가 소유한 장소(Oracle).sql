/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/151137 */


SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR 
WHERE OPTIONS LIKE '%시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE




'''

# 문제
CAR_RENTAL_COMPANY_CAR 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 
자동차 종류 별로 몇 대인지 출력하는 SQL문을 작성
이때 자동차 수에 대한 컬럼명은 CARS로 지정하고, 
결과는 자동차 종류를 기준으로 오름차순 정렬



# 풀이
WHERE 절에서 FROM절에서 읽어온 테이블에서 조건에 맞는 결과만 갖도록 간추림
GROUP BY 절에서 WHERE조건으로 간추린 데이터를 선택한 컬럼으로 GROUPING 작업을 한 결과
ORDER BY 로 행의 순서 정렬

'''
