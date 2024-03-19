def solution(x1, x2, x3, x4):
    answer = True
    x5 = x1 or x2   #합집합
    x6 = x3 or x4   
    answer = x5 and x6  #교집합
    return answer

# 한 줄 코드 : return True if (x1 or x2) and (x3 or x4) else False