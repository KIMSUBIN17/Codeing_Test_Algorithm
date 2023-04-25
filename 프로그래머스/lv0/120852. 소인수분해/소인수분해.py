from collections import OrderedDict

def solution(n):
    answer = []
    d=2
    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            d += 1
    return list(OrderedDict.fromkeys(answer))

'''
OrderedDict.fromkeys 이용하는 방법이 가장 빠름 
순서유지한 상태로 리스트 중복 제거 가능

set():순서유지x 중복값 제거 

'''