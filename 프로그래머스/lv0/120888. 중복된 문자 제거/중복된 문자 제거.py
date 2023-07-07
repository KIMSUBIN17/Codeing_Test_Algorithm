def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

'''
# 딕셔너리 사용-리스트의 중복 제거할때 사용
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
'''