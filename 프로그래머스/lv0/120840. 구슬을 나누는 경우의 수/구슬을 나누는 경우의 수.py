import math

def solution(balls, share):
    return math.comb(balls,share)

'''
*조합 : 서로 다른 n개의 수 중 m개를 뽑는 것
comb(n,m) : nCm 조합 값을 반환
'''