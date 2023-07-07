# 다시풀어보기
def solution(board):
    N = len(board)      # 방향탐색할때 경계값 걸기위해
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]   #8방향 탐색위한 
    
    #지뢰설치
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                boom.append((i,j))  #지뢰일때 인덱스append
    # 지뢰설치된 곳 주변에 폭탄 설치
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1
    # 폭탄 없는 곳 count
    count = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                count += 1
    return count