/*문제링크: https://programmers.co.kr/learn/courses/30/lessons/59038 */

SELECT datetime as "시간"
from(select datetime 
     from animal_ins order by datetime asc)
where rownum = 1;

/*rownum으로 첫번째 값만 추출*/