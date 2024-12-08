import sys
 
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
 
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
 
for m in M_list:
    left = 0
    right = N - 1
 
    while left <= right:
        mid = (left + right) // 2
        if m > N_list[mid]:
            left = mid + 1
        elif m < N_list[mid]:
            right = mid - 1
        else:
            left = mid
            right = mid
            break
            
    if left == mid and right == mid:
        print(1)
    else:
        print(0)




'''
오답노트 : 처음에는  이중for문으로 문제를 풀었으나,시간 초과 발생
--> 이진 탐색 사용!(인덱스를 활용한 이진탐색 사용으로 시간 단축)

* 이진탐색
- O(logN)
- 정렬된 자료를 반씩 나누어 탐색
target: 찾고자 하는 값
data: 오름차순으로 정렬된 list
start: data의 첫 번째 인덱스
end: data의 마지막 인덱스
mid: start와 end의 중간값

자료의 중간(mid) 값이 찾고자 하는 값(target)인지 확인
아니라면 자료의 중간(mid)값과 찾고자 하는 값(target)을 비교하여 start, end 이동
구현
# data 중에서 target 을 검색하여 index 값을 return 하고,
# 없으면 None을 return
 
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1
 
    while start <= end:
        mid = (start + end) // 2
 
        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
 
    return None
'''
