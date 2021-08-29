/*링크 : https://programmers.co.kr/learn/courses/30/lessons/59405 */

SELECT NAME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME)
WHERE ROWNUM = 1;
