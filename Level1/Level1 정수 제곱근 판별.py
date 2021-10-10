/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12934 */


def solution(n):
    answer = 0
    num = n ** 0.5
    
    if num == int(num):
        answer = (num+1) ** 2
    else:
        return -1
    return answer


'''

#풀이 
1. 주어진 수가 정수의 제곱인지
2. 정수의 제곱이라면 정수(제곱근)에 1 더한수를 제곱한 수를 리ㄹ턴
3. 정수의 제곱이 아니라면 -1 리턴
-> 원래 값과 정수로 바꾼 값이 같은 지 확인 => 어떤 값이 정수인지 확인하는 방법

-> 생각할 것 : 제곱근 구하는 함수, 정수인지 자료형 판별


#다른 사람 풀이
1-(1). sqrt()함수사용

def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

-> **(1/2)가 제곱근임(암기)
import math안써도 가능
math라이브러리의 sqrt(x)함수는 x의 제곱근을 반환


1-(2). import math 사용

import math

def solution(n):
    a = math.sqrt(n)
    if int(a) == a:
        return (a+1)**2
    else:
        return -1

원래 값과 정수로 바꾼 값이 같은 지 확인 => 어떤 값이 정수인지 확인하는 방법
ex. 5.0 과 int(5.0)이 같으면 그 값은 정수값임을 확인


2. 1번을 더 파이써닉하게 한줄로 
def solution(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or -1

->return에 and와 or도 쓸 수 있음


3. 인덱싱사용해 '.0'을 비교해 정수 판별

def solution(n):
    #x+1의 제곱 or -1을 저장할 변수
    answer = 0
    #양의 정수 n의 제곱근을 저장하는 변수
    x = n ** 0.5
    
    #n이 양의 정수 x의 제곱이라면
    if str(x)[-2:] == '.0':
        #x+1의 제곱을 리턴
        answer = (x + 1) ** 2
    #n이 양의 정수 x의 제곱이 아니라면
    else:
        #-1을 리턴
        answer = -1
    
    return answer

-> x의 뒤에서부터 2글자가 '.0'인지 확인해 정수판별


-------------
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.
입출력 예
n	return
121	144
3	-1
입출력 예 설명
입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.




'''