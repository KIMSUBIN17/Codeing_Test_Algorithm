def solution(myString):
    answer = list(filter(None,myString.split("x")))
    return sorted(answer)

'''
filter()gkatn
- 특정조건에 맞는 요소만 출력
'''