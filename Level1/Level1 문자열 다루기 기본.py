/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12918 */

def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() :
            return True
    return False

'''
문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
입출력 예
s	return
"a234"	false
"1234"	true


#풀이 -> isdigit()함수 기억하기
isdigit()함수 이용해 s.isdigit()하면 숫자인지 아닌지 판별가능
cf) isalpha() : 문자열인지 아닌지 확인

#다른사람풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

단순풀이-isdigit()을 모른다면
def solution(s):
    if (len(s) == 4) or (len(s) == 6):
        for i in s:
            if i not in '1234567890':
                return False
        return True
    else:
        return False 




'''