SELECT ANIMAL_ID,NAME,
    CASE
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
        END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;



'''
#다른 풀이
SELECT ANIMAL_ID, NAME,
CASE WHEN SEX_UPON_INTAKE LIKE 'Intact%' THEN 'X'
ELSE 'O'
END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

#문제
보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다. 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.


#CASE표현식:여러 범주의 조건 각각 대응해 값 출력
select case when 조건1 then 출력1
            when 조건2 then 출력2
            ...
            when 조건N then 출력N
	        else 출력N+1
       end "출력할컬럼이름Z"
from 테이블이름;


#CASE WHEN문
CASE WHEN [조건] THEN [리턴값]
     WHEN [조건] THEN [리턴값]
     ELSE [리턴값] # 생략하면 NULL 리턴
     END # 생략 불가
     AS [재명명필드명]

->decode사용하면 like비교를 할 수 없음->case문사용해야함


'''

