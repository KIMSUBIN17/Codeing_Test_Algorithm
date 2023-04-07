from collections import deque

def solution(numbers, direction):
    answer = []
    
    if direction == 'right':
        answer.append(numbers[-1])
        
        for i in numbers[0:-1]:
            answer.append(i)
    else:       #left
        for i in numbers[1:]:
            answer.append(i)
        answer.append(numbers[0])
    return answer


'''
리스트 슬라이싱 : numbers[a:b] 
-> a인덱스의 원소부터 b이전 인덱스의 원소까지 포함
numbers[0:-1] --> 0번째 인덱스의 원소부터 -1번째 인덱스의 이전원소까지 -> 
numbers[0:-1] 이고 numbers=[1,2,3]이면
0번째 인덱스(원소1)부터 -1번째 인덱스의 이전(3)까지 즉 원소1부터 원소3까지가 된다--> 위 소스에서는 배열 numbers의 처음부터 끝까지 for문을 돌림 

-- 다른사람 풀이 참고/커밋하고 다른 사람 풀이 추가 첨부하기
리스트 회전하는 문제 --> deque 자료형 사용해보자 ! 
함수안에 음수 넣으면 왼쪽회전 / 양수 넣으면 오른쪽회전

# 다른사람 풀이1 -  rotate() 랑 deque 사용
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else :
        numbers.rotate(-1)
        
    return list(numbers)


'''