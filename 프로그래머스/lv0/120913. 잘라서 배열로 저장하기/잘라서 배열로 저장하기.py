def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str),n)]

'''
0부터 my_str 끝까지의 범위 동안 n씩 반복하여 n범위만큼 출력 
'''