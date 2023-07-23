def solution(arr, queries):
    answer = []
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    return arr



'''
#다른사람의 풀이
def solution(arr, queries):
    new_arr = arr
    # 순서 바꾸기
    for q in queries:
        first_num = new_arr[q[0]]
        second_num = new_arr[q[1]]
        new_arr[q[0]] = second_num
        new_arr[q[1]] = first_num
    return new_arr
'''
