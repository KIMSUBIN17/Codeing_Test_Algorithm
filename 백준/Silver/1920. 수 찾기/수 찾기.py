import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
A = set(map(int, input().split()))  # A를 집합으로 변환
M = int(input())
B = list(map(int, input().split()))

# 결과 출력
for x in B:
    print(1 if x in A else 0)


'''
집합 사용 풀이
1. A를 set으로 변환하여 각 원소를 탐색할 때 평균적으로 O(1)로 처리
2. 탐색
B의 각 원소 x가  A에 존재하는지 x in A로 판별해 존재하면 1, 없으면 0으로 출력
3. 출력 
B의 원소 순서대로 결과 출력 

'''
