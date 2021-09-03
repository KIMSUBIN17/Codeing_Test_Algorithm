/*문제링크: https://programmers.co.kr/learn/courses/30/lessons/59415 */

select datetime
from (select datetime from animal_ins 
     order by datetime desc )
where rownum = 1;

/*datetime을 최신순으로 정렬하고 rownum으로 첫번째 값만 추출*/