def solution(n):
    answer = 0
    
    for i in range(n):
        if n%(i+1) == 0:
            answer += 1
    return answer

'''
1부터 n까지 반복하며 나누어 떨어지는 수들을 더해 리턴함
'''