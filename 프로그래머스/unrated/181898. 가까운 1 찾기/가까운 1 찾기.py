def solution(arr, idx):
    answer = -1     # 해당사항 없으면 그냥 -1 출력
    for i, num in enumerate(arr):
        if idx <= i and num == 1:
            return i
    return answer