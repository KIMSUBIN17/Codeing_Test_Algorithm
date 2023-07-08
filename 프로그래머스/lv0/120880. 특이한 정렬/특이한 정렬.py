# 다시 풀어보기
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

'''
n과의 거리의 절대값 =  abs(x-n)에 대해 정렬하고,
abs(n-x)가 같으면 n-x가 큰 값을 먼저 정렬
'''