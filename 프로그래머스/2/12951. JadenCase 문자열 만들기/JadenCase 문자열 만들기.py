def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        # capitalize() : 맨 첫글자만 대문자로 변환
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer
    
'''
공백분리 시 그냥 split()만 하면 테스트케이스 몇개에서 오류 발생
split()은 공백이 몇개든 모든 공백을 하나로 처리하기때문에 사용시 s는 알파벳,숫자, 공백문자(" ")로 이루어졌다는 조건에 걸림
split(' ') 사용하면 문자열 사이사이에 있는 공백만 분리 포인트로 삼을 수가 있음
'''