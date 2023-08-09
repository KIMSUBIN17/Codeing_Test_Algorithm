def solution(str_list, ex):
    answer = ''
    for part_string in str_list:
        if not ex in part_string:
            answer += part_string
    return answer