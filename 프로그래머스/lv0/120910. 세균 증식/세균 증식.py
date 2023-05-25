def solution(n, t):
    answer = n
    
    for i in range(t):
        answer *= 2
    return answer

'''
# 다른 사람의 풀이
def solution(n, t):
    return n << t

비트연산자 사용
<< : 비트 왼쪽 시프트 ; a의 비트를 b번 왼쪽으로 이동
'''