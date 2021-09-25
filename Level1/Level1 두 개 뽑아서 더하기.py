/*링크 : https://programmers.co.kr/learn/courses/30/lessons/68644 */

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer

'''
문제 설명
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.
입출력 예
numbers	result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]
입출력 예 설명
입출력 예 #1

2 = 1 + 1 입니다. (1이 numbers에 두 개 있습니다.)
3 = 2 + 1 입니다.
4 = 1 + 3 입니다.
5 = 1 + 4 = 2 + 3 입니다.
6 = 2 + 4 입니다.
7 = 3 + 4 입니다.
따라서 [2,3,4,5,6,7] 을 return 해야 합니다.
입출력 예 #2

2 = 0 + 2 입니다.
5 = 5 + 0 입니다.
7 = 0 + 7 = 5 + 2 입니다.
9 = 2 + 7 입니다.
12 = 5 + 7 입니다.
따라서 [2,5,7,9,12] 를 return 해야 합니다.

#풀이
모든 요소에 대해 더하고 나온 결과값에서 중복되는 값이 있는지 확인해서 중복 배제
if numbers[i]+numbers[j] not in answer : numbers[i]와 numbers[j]더한값이 합을 저장할 answer 리스트에 있는지 확인해서 중복을 배제함
->테스트 7번에서 급격히 속도가 느려짐

#다른사람 풀이 

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)

파이썬 기본 라이브러리인 itertools의 combinations(순열)이라는 내장함수 사용해 인자값에 따라 해당 요소로 구할 수 있는 모든 조합 리턴
ex) combinations(numbers, 2)는 numbers 리스트 안에 2개의 요소로 구할 수 있는 모든 조합을 반환

>더 짧은 코드
from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,2)])))



'''