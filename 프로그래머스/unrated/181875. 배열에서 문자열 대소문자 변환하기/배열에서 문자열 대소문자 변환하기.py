def solution(strArr):
    answer = []
    
    for i,s in enumerate (strArr):
        if i % 2 == 0 :
            answer.append(s.lower())
        else:
            answer.append(s.upper())
    return answer


'''
enumerate함수 사용해 인덱스와 원소를 동시에 받아옴
최종적으로 문자열이 변환된 리스트를 리턴
'''