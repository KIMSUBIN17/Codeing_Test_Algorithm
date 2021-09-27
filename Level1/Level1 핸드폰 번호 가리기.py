/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12948 */

def solution(phone_number):
    answer = ''
    
    phone_len = len(phone_number)
    answer = '*' * (phone_len - 4) + phone_number[-4:]
    
    return answer

'''
문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 4 이상, 20이하인 문자열입니다.
입출력 예
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"

#풀이
1. 전화번호 뒷자리 4자리 제외한 나머지 숫자를 전부 *로 가린 정답을 저장할 변수 선언
2. phone_number의 길이를 저장하는 변수 phone_len 선언
3. answer에 phone_len에서 4를 뺀 만큼 *를 넣고, phone_number의 뒷 4자리도 넣어줌
4. answer값 반환

뒷자리 4개 빼고는 *로 바꿔야하므로 (전화번호길이- 4)만큼의 *를 answer에 붙임
그 뒤에 전화번호 뒷자리 4개를 slice ( 음의 정수를 넣으면 원소를 거꾸로 탐색
-> -4이므로 뒤에서부터 4개원소 slice 
-> 콜론(:) 넣어서 시작인덱스와 (끝 인덱스 - 1) 설정가능



#다른사람풀이


'''