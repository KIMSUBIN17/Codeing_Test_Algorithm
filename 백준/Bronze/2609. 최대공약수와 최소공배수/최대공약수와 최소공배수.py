#유클리드 호제법 사용
#두 개의 자연수 입력받기
a,b = map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b = b,a % b
    return a
def lcm(a,b):
    return a * b //gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))




'''
# 파이썬 내장 math 함수 사용
import math

a,b = map(int,input().split())

print(math.gcd(a,b))
print(math.lcm(a,b))
'''

