/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12926 */

def solution(s, n):
    answer = ''
    
    for c in s:
        # c가 공백이라면
        if c == ' ': 
	#공백 그대로 answer에 넣어주고
            answer += ' '
	#다음 문자로 넘어감
            continue
        
        #n만큼 이동한 후의 아스키코드값 저장
        scissor = ord(c) + n
        if (ord(c) in range(ord('A'), ord('Z')+1) and scissor > ord('Z')) or \
            (ord(c) in range(ord('a'), ord('z')+1) and scissor > ord('z')):
            # 1. c가 대문자면서 n을 더했을 때 'Z'를 넘어가는 경우
            # 2. c가 소문자면서 n을 더했을 때 'z'를 넘어가는 경우
            #알파벳의 개수인 26을 빼서 그 값을 answer에 더함
            answer += chr(scissor-26)
        # 'Z'나 'z'를 넘어가지 않는 경우
        else:
            #그냥 scissor값을 answer에 더함    	
            answer += chr(scissor)
        
    return answer

'''
#풀이(다른사람 풀이 참고)
- ord("문자") : 문자를 아스키코드로 변환
- chr(정수) : 입력받은 숫자(아스키코드)에 해당하는 문자로 변환



#다른 사람 풀이

def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)


--------------------
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
입출력 예
s	n	result
"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"
'''