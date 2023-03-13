def solution(my_string):
    answer = ''.join(reversed(my_string))
    return answer

'''
#다른 풀이
def solution(my_string):
    answer = my_string[::-1]
    return answer
    
#추가 설명
리스트 슬라이스 : list[start:endLstep]
step을 -1로 하면 뒤에서부터 순차적으로 가져옴(=리스트 뒤집기)
join() :  '구분자'.join(리스트)형태
매개변수로 들어온 리스트의 값들을 하나의 문자열로 합쳐줌
''.join(list) --> 띄어쓰기 없이 하나로 합쳐짐
join(reversed(list)) : list앞에 reversed 입력하면 들어온 리스트의 순서를 뒤집어서 합쳐줌


'''
