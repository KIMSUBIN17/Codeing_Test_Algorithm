/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/42748 */

def solution(array, commands):
    answer = []
    
    for i in commands:
        start, end, select = i
        slice_arr = array[start-1:end]
        slice_arr.sort()
        answer.append(slice_arr[select-1])
    
    return answer