/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12931 */

def solution(n):
    answer = sum((map(int,list(str(n)))))
    return answer

'''
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수
입출력 예
N	answer
123	6
987	24
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.


#풀이
n을 문자열로 바꿔서 list()에 담으면 각 자리 분리해서 리스트로 담을 수 있음
map()함수 이용하면 입력되는 리스트들에 모두 일정한 함수를 적용시킬 수 있음
->map(int,list)를 하면 list에 있는 모든 요소를 int()함수에 넣은 결과값과 동일
리스트로 나오는 결과를 sum()으로 총합구함

#다른사람풀이
def solution(n):
    return sum([int(i) for i in str(n)])
-> n을 str로 바꾸고 for문 이용해 합을 구한 후 return

def solution(n):
    sum([int(i) for i in str(n)])

>>재귀함수이용
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 


'''