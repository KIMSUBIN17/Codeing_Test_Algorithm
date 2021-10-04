/*링크 : https://programmers.co.kr/learn/courses/30/lessons/86051 */

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer



'''
문제 설명
0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 수 ≤ 9
numbers의 모든 수는 서로 다릅니다.
입출력 예
numbers	result
[1,2,3,4,6,7,8,0]	14
[5,8,4,0,6,7,9]	6
입출력 예 설명
입출력 예 #1

5, 9가 numbers에 없으므로, 5 + 9 = 14를 return 해야 합니다.
입출력 예 #2

1, 2, 3이 numbers에 없으므로, 1 + 2 + 3 = 6을 return 해야 합니다.

#풀이
0~9까지의 수를 범위로 for문을 돌리고, numbers안에 없는 값을 찾으면 answer에 더하고 리턴함

#다른 사람 풀이
1-(1).그냥 풀어서 풀기
def solution(numbers):
    return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])

1-(2). 그냥 풀어서 풀기
def solution(numbers):
    answer = 0
    a = [x for x in range(1,10)]

    for i in numbers:
        for j in a:
            if i == j:
                a.remove(j)

    for x in a:
        answer += x

    return answer

2. set함수 사용

def solution(numbers):
    return sum(set(range(10)) - set(numbers))



'''