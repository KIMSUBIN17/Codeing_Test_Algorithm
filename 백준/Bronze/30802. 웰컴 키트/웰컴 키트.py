from math import ceil

n = int(input())

shorts = list(map(int, input().split()))    #2 3 1 1 2 1을 입력하면, 리스트 shorts는 [2, 3, 1, 1, 2, 1]
# 티셔츠의 묶음 크기 t, 펜의 묶음 크기 p를 입력
t,p = map(int, input().split())

#shorts의 각 요소 x에 대해 x/t를 올림처리하여 필요한 티셔츠 묶음수 계산하고, sum을 한다
print(sum([ceil(x/t) for x in shorts]))

# n // p : 참가자n을 펜 묶음  크기p로 나눈 몫 = 필요한 펜 묶음의 수
# n % p  : 참가자 n을 펜 묶음 크기 p로 나눈 마머지,펜을 나누고 남은 참가자의 수
print(n//p, n%p)
