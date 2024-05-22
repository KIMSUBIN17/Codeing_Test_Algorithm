def solution(board,h,w):
    n = len(board)  #보드의 크기 
    count = 0       #같은 색으로 색칠된 칸의 개수를 저장할 변수 count
    
    #방향 벡터(위, 아래, 왼쪽, 오른쪽)
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    #i가 1~3까지 반복
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        #보드의 범위를 벗어나지 않는지 확인
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
                
    return count
