N,K=map(int,input().split())
arr=[] #약수들을 담은 배열
for i in range(1,N+1):
    if(N%i==0):
        arr.append(i)

if(K<=len(arr)):
    print(arr[K-1])
else:
    print(0)