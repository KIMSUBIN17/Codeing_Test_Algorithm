def solution(n):
    sqrt = n ** (1/2)  # 제곱근
    if sqrt % 1 == 0:  #1로 나눠서 0이면 정수
        return 1
    else:
        return 2
        
'''
# 다른 사람 풀이
import math

def solution(n):
    return 1 if int(math.sqrt(n)) ** 2 == n else 2

'''
        
        
