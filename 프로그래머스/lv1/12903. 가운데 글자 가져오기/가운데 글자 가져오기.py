def solution(s):
    #홀수
    if len(s)%2 == 1:
        return s[len(s)//2]
    #짝수
    else:
        return s[(len(s)//2)-1:(len(s)//2)+1]