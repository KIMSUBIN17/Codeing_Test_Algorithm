def solution(num_list):
    multi = num_list[0]
    sum = num_list[0]
    for num in num_list[1:]:
        multi *= num
        sum += num
    return 1 if multi < sum**2 else 0
        