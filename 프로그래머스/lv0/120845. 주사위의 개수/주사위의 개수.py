def solution(box, n):
    return (int(box[0]//n) * int(box[1]//n) * int(box[2]//n))


'''
#다른사람의 풀이
import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))

- math.prod() : ()안에 있는 모든 iterable 요소들의 곱을 구함
->box안에 있는 모든 값 v들을 n으로 나눈 값의 몫을 모두 곱하는 값을 구하는 것
'''