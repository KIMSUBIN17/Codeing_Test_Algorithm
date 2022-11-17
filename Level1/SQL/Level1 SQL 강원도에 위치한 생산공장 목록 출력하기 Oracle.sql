/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131112 */



SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '%강원도%'
ORDER BY FACTORY_ID ASC;



'''

강원도에 위치한 --> 출력 위해 LIKE % % 사용

다른 표현
WHERE substr(address, 0, 3) = '강원도'


'''
