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



# 탐색문제임을 찾는 핵심
1. 입력 크기를 확인 : 입력 크기와 요구되는 연산 

문제에서 주어진 N,M은 최대 100,000이므로 최악의 경우 N * M = 100,100 * 100,000 = 10^10번 연산 필요

단순 반복문  사용 시  각 B의 모든 원소가 A전체를 순회하는 경우 O(N*M)
N,M크기 때문에 시간초과 가능성 큼


2. 연산의 본질 파악 : 존재 여부를 파악 
문제의 요구사항 : A배열에서 B배열의 각 원소가 존재하는지 찾기 --> 탐색! (특정 데이터를 효율적으로 찾는 방법 설계 필요)

탐색 문제는 보통 다음 알고리즘이 적합:
- 정렬 + 이분 탐색 (정렬 후 효율적으로 검색)
- 해시나 집합 (빠른 조회를 위한 데이터 구조)


3. 효율적인 데이터 구조나 알고리즘 고민
그렇다면, 두 가지 방법 중 어떤 방법이 더 적합할지 고민 --> 입력 구조에서 캐치해볼 것
A 배열은 주어졌고, 이를 여러 번 조회해야함
B 배열의 모든 값을 A에서 찾아야하므로 반복적으로 탐색이 필요함
--> A를 먼저 한번 정렬하거나 구조화 해서 효율적탐색이 가능한가?
    --> 이분탐색 사용 시 O(MlogN)으로 각 값을 탐색 할 수 있음
    A를 정렬 후 B의 각 값을 이분 탐색으로 탐색
--> A를 집합(set)으로 처리하면 좀 더 빠를까?
    --> 평균적으로 O(1)로 처리가능
    A를 집합을으로 변환 후 B의 각 원소x가 A에 존재하는지 x in A로 판별


    
'''
