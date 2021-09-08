/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/42748 */

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

'''
list[시작 : 끝]
- 시작은 포함, 끝은 포함X
start의 인덱스는 + 1이 되어있기때문에 start 인덱스는 - 1을 해준다. 
end는 -1을 하지 않고 그냥 그대로 써준다.
'''