#다시풀어보기
def solution(dots):
    answer = 0
    
    if slope(dots[0],dots[1]) == slope(dots[2],dots[3]):
        answer = 1
    if slope(dots[0],dots[2]) == slope(dots[1],dots[3]):
        answer = 1
    return answer

def slope(dot1, dot2):    #기울기 구하는 함수
    return (dot2[1]-dot1[1]) / (dot2[0] - dot1[0])

'''
평행의 조건
두 직선의 기울기가 동일해야함 / y절편값이 달라야함
'''