def solution(arr, n):
    for idx, val in enumerate(arr):
        if len(arr) % 2 == 0:           #짝수
            if idx % 2 == 1:
                arr[idx] += n
        else:           #홀수
            if idx % 2 == 0:
                arr[idx] += n
    return arr

'''
* enumerate (파이썬 내장함수)
- index와 원소 동시에 접근하면서 루프 돌리기 가능(index 변수 증가 없이)
- for문의 in 부분을 enumerate()함수로 감싸기
- 중첩 for문 작업 -> enumerate() 함수로 작업
'''