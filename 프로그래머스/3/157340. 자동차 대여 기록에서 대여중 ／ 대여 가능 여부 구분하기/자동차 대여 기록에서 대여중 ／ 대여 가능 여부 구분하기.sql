-- 코드를 입력하세요
SELECT CAR_ID
, MAX(CASE WHEN '20221016' BETWEEN TO_CHAR(START_DATE,'YYYYMMDD') AND TO_CHAR(END_DATE,'YYYYMMDD') THEN '대여중'
                                                                          ELSE '대여 가능' 
                                                                          END) AS AVAILAVILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY CAR_ID
ORDER BY CAR_ID DESC

/* #오답노트 
바로 해결하지 못한 이유 : CAR_ID를 출력할 때 CAR_ID를 GROUP BY만 하면 오류가 발생. 적합한 집계함수를 쓰지못함
--> MAX함수 사용해서 가장 최신 날짜의 데이터를 가져오도록함
MAX함수는 GROUP BY 함수와 같이 사용해야하는데 
MAX 함수를 사용하는 이유?
-> "날짜 순에서 가장 최근의 값만 사용하고 싶을 때는 'max'를 사용한다"



*/