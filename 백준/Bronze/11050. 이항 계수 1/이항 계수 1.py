#팩토리얼 계산 위해 math 라이브러리 사용
import math

#n,k 입력받아 정수로 변환
n,k = map(int,input().split())

#이항 계수 계산 공식 사용
res = math.factorial(n) // (math.factorial(k)  *  math.factorial(n-k))

print(res)

'''
팩토리얼 연산은 O(N)이지만, 조건에 따라 N<=10이므로 빠르게 연산 가능
'''