def find(arr):
    mx = 1
    tmp = 1
    for i in range(N):
        for j in range(N-1):  
        	#가로
            if arr[i][j] == arr[i][j+1]: # 연속한지 확인 
                tmp += 1
            else:
                tmp = 1  # tmp 초기화
            if tmp > mx:
                mx = tmp
        tmp = 1  # tmp 초기화
        #세로
        for j in range(N-1):  
            if arr[j][i] == arr[j+1][i]: # 연속한지 확인 
                tmp += 1
            else:
                tmp = 1  # tmp 초기화
            if tmp > mx:
                mx = tmp
        tmp = 1 # tmp 초기화
    return mx

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    a = input()
    for j in range(N):
        arr[i].append(a[j])
mx = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            # 가로줄  바꾸기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            tmp = find(arr)  # 바꾼 배열의 최대값 구하기
            if tmp > mx:
                mx = tmp
            # 되돌리기
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if i + 1 < N:
            # 세로줄 바꾸기
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            tmp2 = find(arr)
            if tmp2 > mx:
                mx = tmp2
            # 되돌리기
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
print(mx)