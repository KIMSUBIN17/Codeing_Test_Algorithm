#중복없이-->순열 사용 / itertools.permutations을 사용하면 순열이 사전순으로 출력됨
from itertools import permutations

#N,M입력받기
N,M = map(int,input().split())

#1~N까지 자연수 중에서 M개를 고른 순열 모두 출력
#순열:순서고려X, 중복X
for seq in permutations(range(1,N+1),M):
    print(' '.join(map(str,seq)))