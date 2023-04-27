def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer


'''
# 다른 사람의 풀이
def solution(my_string):
    return my_string.swapcase()
'''