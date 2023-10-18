def solution(s):
    answer = ''
    s = list(s.split())
    #map함수 사용해 문자열의 각 부분을 정수로 변환
    s_int = list(map(int,s))
    min_s = min(s_int)
    max_s = max(s_int)
    
    return f"{min_s} {max_s}"



'''
더 짧은 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
'''
