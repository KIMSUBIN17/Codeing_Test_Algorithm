N,K=map(int,input().split())
arr=[] #약수들을 담은 배열

#1~N까지반복하면서 N의 약수 찾기
for i in range(1,N+1):
    if(N%i==0):
        arr.append(i)

if(K<=len(arr)):
    #리스트는  0부터 시작하므로 K-1번째 요소가 K번재
    print(arr[K-1])
else:
    print(0)
