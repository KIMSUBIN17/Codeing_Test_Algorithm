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
