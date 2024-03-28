def solution(n):
    arr = [[0]*n for i in range(n)]      # n x n 크기의 모든 원소를 0으로 초기화하는 이차원 배열 생성
    for i in range(n):
         # i=j일때 1로 설정->주 대각선에 해당하는 위치에 1로 설정
        arr[i][i] = 1      
    return arr