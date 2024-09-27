#n = int(input())
import sys
# n = 점의 갯수 (첫번째 입력값)
n=int(sys.stdin.readline())

#각 점의 좌표 (x,y)를 튜플로 이 리스트에 저장
arr=[]

#반복문으로 n개의 점의 좌표 입력받고 
for i in range(n):
    a,b = map(int,input().split())    #map():문자열->정수 변환
    arr.append((a,b))    #변환된 좌표(a,b)를 튜플형태로 arr리스트에 추가 
arr.sort()

for i in range(n):
    print(arr[i][0], arr[i][1])  #x좌표,y좌표
    
'''
이중리스트로 저장 후 sort 정렬
# 속도 개선 위해 input부분에 sys 라이브러리 사용가능
import sys
n=int(sys.stdin.readline())

좌표 --> 튜플 형태로 표현
'''
    
