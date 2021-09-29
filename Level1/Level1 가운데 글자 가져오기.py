/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12903 */

def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() :
            return True
    return False

'''
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
"abcde"	"c"
"qwer"	"we"

#풀이 -> string형태도 배열처럼 s[1] 과 같은 방식으로 사용가능함을 기억
홀수짝수 나눠서 구현


#다른사람풀이
def solution(s):
    center = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[center]
    else:
        return s[center-1:center+1]

1. if문으로 문자열이 짝수인지 홀수인지 구분
2. 짝수라면 input값을 2로 나눈 값을 i라고 했을 때, i - 1 ~ i 까지의 문자열을 반환
3. 홀수라면 2번의 i번째 문자열 그대로 return 
->파이썬 슬라이싱은 [start : end]일 때 end-1까지 리턴


def string_middle(str):
    # 함수를 완성하세요
    return str[(len(str)-1)//2:len(str)//2+1]





'''