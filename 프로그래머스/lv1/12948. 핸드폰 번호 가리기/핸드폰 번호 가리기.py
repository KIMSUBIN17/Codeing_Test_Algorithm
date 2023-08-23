def solution(phone_number):
    return '*'*len(phone_number[:-4]) + phone_number[-4:]
# [:-4] : 처음부터 -3까지 / [-4:] : -4부터 끝까지



'''
def solution(phone_number):
    answer = ''
    
    phone_len = len(phone_number)
    answer = '*' * (phone_len - 4) + phone_number[-4:] 
    
    return answer
'''