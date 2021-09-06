SELECT ANIMAL_ID,NAME,
    CASE
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
        END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;



'''
CASE표현식:여러 범주의 조건 각각 대응해 값 출력
select case when 조건1 then 출력1
            when 조건2 then 출력2
            ...
            when 조건N then 출력N
	        else 출력N+1
       end "출력할컬럼이름Z"
from 테이블이름;
'''

