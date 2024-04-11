def solution(board, k):
    answer = 0      #모든 합 저장할 정답answer초기화 
    
    for i in range(len(board)):     #board 각 행을 순회 
        for j in range(len(board[i])):  #board[i]의 각 열 순회
            #현재 순회중인 요소의 행 인덱스 i와 열 인덱스 j를 합한 값이 k보다 작거나 같다면 해당 값을 answer에 더함
            if i+j <= k:
                answer += board[i][j]
    return answer