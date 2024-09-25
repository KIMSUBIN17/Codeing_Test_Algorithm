#서로 다른 N개의 자연수의 합 = S
# 자연수S의 값을 입력받음
n = int(input())

sum = 0
result = 0        #정답

#1부터 n까지 더해가다가 n보다 큰 값이 나오면 그 직전 수가 정답
for i in range(1,n+1):
    sum+=i
    result += 1
    if sum>n:    #N개의 자연수의 합이 sum보다 커지면
        result -= 1
        break
print(result)
