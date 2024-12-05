import sys
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    num= int(input())
    if num == 0:        #0일 경우, 가장 최근 값을 제거
        stack.pop()
    else:            #0이 아닐 때 값을 추가
        stack.append(num)
        
        
print(sum(stack))