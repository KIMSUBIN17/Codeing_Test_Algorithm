/*링크 : https://programmers.co.kr/learn/courses/30/lessons/77884 */

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count=0     #약수의 개수 담을변수
        
        for j in range(1,i+1):		#1부터 i까지 증가하면서 약수를 찾아냄
            if i % j == 0:		#나누어 떨어지는 수는 약수
                count += 1		#약수라면 count를 증가시킴
        if count % 2 == 0:		#약수의 개수가 짝수인지 홀수인지
            answer += i		#약수의 개수가 짝수이면 더해줌
        else:			
            answer -= i		#약수의 개수가 홀수이면 빼줌
    
    return answer



'''
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예
left	right	result
13	17	43
24	27	52
입출력 예 설명
입출력 예 #1

다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.
수	약수	약수의 개수
13	1, 13	2
14	1, 2, 7, 14	4
15	1, 3, 5, 15	4
16	1, 2, 4, 8, 16	5
17	1, 17	2
따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.

#풀이
0~9까지의 수를 범위로 for문을 돌리고, numbers안에 없는 값을 찾으면 answer에 더하고 리턴함

#다른 사람 풀이
1. 제곱수 사용


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


->약수의 개수가 홀수개인 모든 수는 제곱수다


2. 파이썬 math라이브러리 sqrt()함수 사용
sqrt(x) : x의 제곱근을 반환



import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer




'''