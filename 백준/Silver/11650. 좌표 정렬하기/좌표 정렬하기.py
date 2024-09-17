#n = int(input())
import sys
n=int(sys.stdin.readline())

arr=[]

for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()

for i in range(n):
    print(arr[i][0], arr[i][1])
    
'''
이중리스트로 저장 후 sort 정렬
# 속도 개선 위해 input부분에 sys 라이브러리 사용가능
import sys
n=int(sys.stdin.readline())
'''
    