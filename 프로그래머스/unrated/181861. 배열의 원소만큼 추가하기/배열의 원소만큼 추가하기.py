def solution(arr):
    X = []     # 아무 원소도 들어있지 않은 빈 배열 선언
    
    for num in arr:
        X.extend([num]* num)
    return X