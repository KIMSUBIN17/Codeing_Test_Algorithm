/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/59044 */

SELECT *
FROM(
    SELECT A.NAME, A.DATETIME
    FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B
    ON A.ANIMAL_ID = B.ANIMAL_ID
    WHERE B.ANIMAL_ID IS NULL
    ORDER BY A.DATETIME
)
WHERE ROWNUM < 4;


'''
#문제
아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.

ANIMAL_INS 테이블은 동물 보호소에 <들어온> 동물의 정보를 담은 테이블입니다. ANIMAL_INS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, <보호 시작일>, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

ANIMAL_OUTS 테이블은 동물 보호소에서 <입양 보낸> 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, <입양일>, 이름, 성별 및 중성화 여부를 나타냅니다. ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.


왼쪽 테이블 기준으로 LEFT JOIN 수행(왼쪽 테이블 전체 + 오른쪽 테이블에서 조건에 해당하는 부분만 조인)
ROWNUM과 인라인 뷰 사용해 DATETIME을 내림차순 정렬
ROWNUM <4 : ROWNUM이 4미만인 값 추출

ROWNUM=1 과 같은 방식이 안되는 이유
ROWNUM은 테이블 WHERE절이 실행될 때 조건에 맞으면 1부여
맞지않으면 번호 부여하지 않고 버리는 방식
-> ROWNUM=1이 아니면 어떤 결과도 추출될수가 없음!

참고링크 : https://jhnyang.tistory.com/454

'''
