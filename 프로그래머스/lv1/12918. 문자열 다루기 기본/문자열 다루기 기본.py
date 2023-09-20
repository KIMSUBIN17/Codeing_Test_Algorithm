def solution(s):
    #문자열s의 길이가 4 or 6이고
    if len(s) == 4 or len(s) == 6:
        #문자열 s가 모두 숫자로 구성되었으면 True
        if s.isdigit():
            return True
    return False


