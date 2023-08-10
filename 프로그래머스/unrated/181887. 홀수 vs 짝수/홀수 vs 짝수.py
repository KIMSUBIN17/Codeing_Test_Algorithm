def solution(num_list):
    odd_sum = sum(num_list[1::2])
    even_sum = sum(num_list[0::2])
    if odd_sum < even_sum:
        return even_sum
    else:
        return odd_sum