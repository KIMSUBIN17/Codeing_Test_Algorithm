from itertools import combinations        #itertools 모듈 내장 함수_조합 구하는데 사용

#자연수N,M 입력받기
N, M = map(int, input().split())

#1~N까지 중복없이  M개를 고르는 조합
for seq in combinations(range(1, N+1), M):
    print(' '.join(map(str, seq)))
