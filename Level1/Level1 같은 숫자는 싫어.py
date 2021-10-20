/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12906 */

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer


'''
#풀이
주어진 배열 arr에서 중복을 제외한 list를 반환하는 문제
여기서 중복 제거란 연속된 중복을 제거한다는 의미
연속된 중복 제거 후 반환되는 리스트는 순서가 유지되어야 하므로 set 자료형 사용할 수 없음.
(set은 전체 배열에서 중복을 제거하고 " 그 순서를 정렬하기"때문)

->완전 탐색이 필요

1. 첫번째 값 배열에 추가
answer 리스트에서 첫번째 리스트의 인덱스는 항상 arr의 인덱스 값을 가질 것이기 때문에 초기값은 arr의 첫번째 인덱스로 잡아줌

2. 이전값과 현재값 비교해 같지 않으면 answer배열에 추가
그 이후 2번째 인덱스부터 arr 배열의 인덱스까지는 앞,뒤 값을 비교해 다르다면 이전 값을 append해줌


#다른 풀이

def solution(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result


* 슬라이싱 사용
def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

핵심:a[-1:]
a[-1:]는 a 값의 가장 뒤의 값을 list로 만들었기 때문에, list가 아닌 i랑 list인 a[-1:]값이랑 같은지 물어보면 다른게 나옴


문제 설명
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

제한사항
배열 arr의 크기 : 1,000,000 이하의 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
입출력 예
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]

'''
