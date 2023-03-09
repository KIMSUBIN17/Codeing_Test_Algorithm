def solution(n):
    if n%7 == 0:
        answer = n/7
    else:
        answer = n//7+1
    return answer

'''
7로 나누어 떨어지는 경우는 그냥 7로 나눈 수
7로 나누어 떨어지지 않으면 +1판
'''