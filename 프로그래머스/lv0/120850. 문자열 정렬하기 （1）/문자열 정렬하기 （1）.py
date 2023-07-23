def solution(my_string):
    return sorted([int(i) for i in str(my_string) if i.isdigit()])


'''
# 다른 풀이
answer = []
for i in my_string:
    if i.isdigit():     #값이 숫자가 맞다면
        answer.append(int(i))
    answer.sort()
    return answer

'''