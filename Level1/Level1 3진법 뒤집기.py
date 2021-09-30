/*링크 : https://programmers.co.kr/learn/courses/30/lessons/68935 */

def solution(n):
    answer = ''
    
    #3진법 변환
    while n > 0 :
        n,m = divmod(n,3)	#n을 3으로 나눈 몫과 나머지
        answer += str(m)
    
    #10진법으로 변환
    return int(answer,3)

    # result = int(answer, 3): 간단하게 3진법으로 변환하는 방법   
    


'''
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.


입출력 예
n	result
45	7
125	229

#풀이
1. 주어진 자연수를 3진법으로 변환
2. 내장함수 divmod()사용해 3진법으로 변환
3. 2번에서 구한 나머지를 순차적으로 추가하면 3진법으로 변환하면서 뒤집기 가능
4. int()함수 이용해 다시 10진법으로 교체

- divmod() : 몫과 나머지를 리턴합니다. 리턴 값이 2개이므로 튜플을 사용합니다.
- int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌

#다른사람 풀이 

def solution(n):
    return "수박"*(n//2) + "수"*(n%2)
n을 2로 나눈 값이 반복되는 횟수
그 횟수만큼 '수박'을 붙여주고, 홀수일때 '수'를 한번 더 붙임

'''