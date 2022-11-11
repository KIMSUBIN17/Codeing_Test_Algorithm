/* 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/132201 */


SELECT PT_NAME, PT_NO, GEND_CD, AGE, NVL(TLNO,'NONE') AS TLNO
FROM PATIENT 
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME ASC



/*
여러개의 조회 조건 필요할 때는 ORDER BY 절에 두개 쓰면됨
결과값에서 데이터가 없으면 NONE으로 표시되게 하라 했기 때문에 NVL 사용해 NULL값이면 NONE값 넣어줌

*/
