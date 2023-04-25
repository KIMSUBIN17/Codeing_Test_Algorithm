def solution(my_string):
    return sorted([int(i) for i in str(my_string) if i.isdigit()])
 