def solution(n, numlist):
    return ([i for i in numlist if i % n ==0])



# 다른 사람 풀이
'''
1. lambda식 사용
def soultion(n, numlist):
    return list(filter(lambda v: v%n==, numlist))

'''