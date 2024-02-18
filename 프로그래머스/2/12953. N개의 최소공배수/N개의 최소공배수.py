import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    #첫번재 원소로 초기화--> 계산할 최소공배수의 초기 값 설정
    answer = arr[0]  
    #배열 두번째 원소부터 마지막 원소까지 반복
    for i in range(1, len(arr)):
        #각 원소와 answer의 최소공배수를 계산하여 answer에 저장
        #현재까지 계산된 최소공배수와 배열의 다음 원소와의 최소공배수 계산
        answer = lcm(answer, arr[i])
    return answer
