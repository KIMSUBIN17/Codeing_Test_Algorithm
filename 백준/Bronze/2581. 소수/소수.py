M = int(input())
N = int(input())

answer = []
for i in range(M,N+1):
    for j in range(2,i+1):
        if j== i:
            answer.append(i)
        if i % j == 0:
            break
            
if not answer:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])