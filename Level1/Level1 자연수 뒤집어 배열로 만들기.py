/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12932 */

def solution(n):
    return [int(i) for i in str(n)][::-1]

'''
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

#풀이
문자열 거꾸로 -> [::-1]
if) alph = "ABCD"
print(alph = [::-1] ->DCBA

#다른사람 풀이 : map()사용
def solution(n):
    return list(map(int,reversed(str(n))))

'''