n = int(input())
arr = list(map(int,input().split()))
arr.sort()
res = 0
time = 0
for i in range(n):
    time+= arr[i]
    res += time
print(res)