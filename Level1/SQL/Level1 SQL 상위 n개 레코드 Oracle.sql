/*링크 : https://programmers.co.kr/learn/courses/30/lessons/59405 */

SELECT NAME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME)
WHERE ROWNUM = 1;

'''
ROWNUM : 각 행에 대한 일련번호. 선택된 테이블의 레코드에 1부터 순차적으로 번호부여
오라클에서는 테이블 생성하면 ROWNUM이라는 임시칼럼 제공
ORDER BY 절 이용해 레코드정렬 할때는 원하는 순서대로 번호 부여X
-한계점
1. ROWNUM이 부여되는 순서는 테이블에 먼저 INSERT된 레코드의 순서대로 번호가 부여되기 때문에 정렬을 하더라도 입력된 순서가 바뀌지는 않음
2. 숫자가 1부터 반영되기 때문에 ROWNUM 중간값으로 시작되는 조건의 레코드 검색불가
SELECT ROWNUM, ENAME, SAL FROM EMP WHERE ROWNUM > 5; 
->검색불가
->어떤 조건이든 시작하는 ROWNUM은 1부터 시작되어야 하기 때문에
->해결위해 인라인 뷰(INLINE VIEW)사용

*인라인뷰 : FROM절에 사용되는 서브쿼리(SQL문 내부에 일시적으로 뷰를 정의해 사용)
인라인 뷰 사용해 새로운 테이블 일시적으로 생성하고 ROWNUM이용해 쿼리문 실행하면 원하는 결과 검색 가능

->인라인 뷰에 의해 ROWNUM이 1부터 새로 부여

'''
