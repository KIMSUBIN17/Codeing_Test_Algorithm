def solution(strArr):
    answer = []
    
    #인덱스 i와 해당 인덱스의 문자열 s를 for문으로 반복
    for i,s in enumerate (strArr):
        if i % 2 == 0 :
            answer.append(s.lower())
        else:
            answer.append(s.upper())
    return answer


'''
enumerate함수 사용해 인덱스와 원소를 동시에 받아옴
최종적으로 문자열이 변환된 리스트를 리턴

i : 인덱스 
s : 해당 인덱스에 위치한 원소(문자열)
enumerate를 사용하여 반복문을 돌 때 인덱스와 값을 함께 사용할 수 있음
'''