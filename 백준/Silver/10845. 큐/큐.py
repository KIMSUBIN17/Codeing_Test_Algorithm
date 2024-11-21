from collections import deque
import sys

n = int(sys.stdin.readline()) 

dq = deque()

for _ in range(n):
    s = sys.stdin.readline().split() 
    if s[0] == 'push':
        dq.append(s[1])
    elif s[0] == 'pop':
        if len(dq) != 0:    #큐에 항목이 있으면 pop
            print(dq.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(dq))
    elif s[0] == 'empty':    #큐가 비어있으면 1, 큐에 항목이 있으면 0
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':    #맨 앞 정수 출력
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)
       
    
# 스택 --> stack 리스트, 큐 --> deque 사용            
# stack --> stack.pop(0)
# deque --> dq.popleft() 