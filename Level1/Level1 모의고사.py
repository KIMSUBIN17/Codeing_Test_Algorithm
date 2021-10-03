/*링크 : https://programmers.co.kr/learn/courses/30/lessons/42840 */

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.


#다른사람풀이를 참고한 풀이
1. 수포자들의 데이터를 list형태로 저장
2. 반복문으로 answer값과 수포자들이 찍은 값을 비교 후 각 사람의 점수를 score에 저장
3. score에서 가장 큰 값과 다른 모든 값을 비교해 일치하면 해당 인덱스에 +1 한 값을 result에 삽입함(append 이용)

#사용한 함수 정리
1. enumerate() 함수
for 문과 함께 쓰이는 함수로 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값과 함께 리턴

data = ['a', 'b', 'c', 'd']
for idx, value in enumerate(data):
	print(idx, value)

>>출력:
0 a
1 b
2 c
3 d

인덱스 시작 값을 정할 수도 있음

data = ['a', 'b', 'c']
for idx, value in enumerate(data, start=100):
	print(idx, value)

>>출력:
100 a
101 b
102 c

2. max함수
인자의 가장 큰 값 반환
a = [4, 3, 2, 1, 9]
print(max(a))   # 9 출력

b = 'Hello World'
print(max(b))   # r 출력


'''