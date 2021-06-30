SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID;

//NAME=NULL 은 말 그대로 이름이 NULL인 경우
//여기서 말하는 NULL은 데이터가 정의되어있지 않은 경우이므로  IS NULL을 사용해야함