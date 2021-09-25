/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12922 */

def solution(n):
    answer = ''
    
    for i in range(n):
        if(i%2 == 0):
            answer += '수'
        else:
            answer += '박'
    return answer

'''
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.

#풀이
n번 반복. 2로 나누어서 나머지가 0이 되면(짝수)이면 '수'를 붙이고, 홀수이면 '박'을 answer문자열에 더해줌. 마지막에 answer값을 리턴

#다른사람 풀이 

def solution(n):
    return "수박"*(n//2) + "수"*(n%2)
n을 2로 나눈 값이 반복되는 횟수
그 횟수만큼 '수박'을 붙여주고, 홀수일때 '수'를 한번 더 붙임

'''