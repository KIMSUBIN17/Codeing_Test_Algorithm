def solution(num_list):
    answer = [num%2 for num in num_list]
    return [answer.count(0), answer.count(1)]



'''
def solution(num_list):
    even_num = 0
    for num in num_list : 
        if num % 2 == 0:
            even_num += 1
        else : 
            continue
    return [even_num, len(num_list)-even_num]
'''