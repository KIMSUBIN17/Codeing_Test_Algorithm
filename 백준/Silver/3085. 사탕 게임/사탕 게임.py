# 배열 arr에서 연속된 사탕의 최대 개수를 찾는 함수
def find(arr):
    mx = 1    #연속된 사탕의 최대 개수를 저장할 변수_최소 1개 이상은 연속되므로 1로 초기화
    tmp = 1    #연속된 사탕을 임시로 세는 변수_연속된 사탕을 세기 시작할 때 1로 초기화
    for i in range(N):    #i->보드의 각  행
        for j in range(N-1):  #j는 해당 행에서 각 열을 순차적으로 탐색 ->n-1까지탐색하는 이유 : j+1과 비교해야하기때문
        	#가로로 연속된 사탕 확인
            if arr[i][j] == arr[i][j+1]: # 연속한 사탕이 같으면    
                tmp += 1        #연속된 사탕 갯수 +1
            else:            #연속된 사탕 개수 다르면
                tmp = 1  # 연속되지 않으면 다시 1로 초기화 
            if tmp > mx:
                mx = tmp    #현재 연속된 사탕의 수가 최댓값보다 크면 갱신
        tmp = 1  # 한 줄이 끝나면 연속된 사탕 수 초기화 = tmp 초기화
        #세로로 연속된 사탕 확인
        for j in range(N-1):  
            if arr[j][i] == arr[j+1][i]: # 현재 사탕과 바로 아래 사탕이 연속적인지 비교
                tmp += 1
            else:
                tmp = 1  # tmp 초기화
            if tmp > mx:
                mx = tmp
        tmp = 1 # tmp 초기화
    return mx

N = int(input())        #보드의 크기 n입력받기
arr = [[] for _ in range(N)]        #n x n 보드 초기화_크기가 n인2차원 배열 초기화
for i in range(N):
    a = input()
    for j in range(N):
        arr[i].append(a[j])    #각 줄을 리스트로 저장 / a[j]-->각 칸에 들어있는 사탕의 색
mx = 0        #최대 연속 사탕 수를  저장할 변수 0으로 선언
# 이중 반복문으로 보드의 모든칸을 확인
#각 칸의 사탕을 인접한 칸과 교환하여 최대 연속 사탕을 계산할 준비
for i in range(N):
    for j in range(N):
        if j + 1 < N:        #오른쪽 칸이 존재하는지 확인
            # 가로로 인접한 칸과 사탕 교환
            # 인접한 두 칸의 사탕을 교환한 후, find함수 호출하여 최대 연속된 사탕 수 계산
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            tmp = find(arr)  # 교환 후 연속된 사탕 최대값 구하기
            if tmp > mx:
                mx = tmp    #최댓값 갱신
            # 교환한 사탕 다시 원상 복구
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