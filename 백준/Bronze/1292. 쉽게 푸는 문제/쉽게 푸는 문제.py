# 구간A,B 숫자 입력받기
a,b = map(int,input().split())
arr=[0]

for i in range(1,b+1):
    for j in range(i):
        arr.append(i)        #i를 1번 반복하여 리스트에 추가

#구간 A에서 B까지의 합 구하기(리스트의 인덱스는 0부터 시작하므로)
print(sum(arr[a:b+1]))
