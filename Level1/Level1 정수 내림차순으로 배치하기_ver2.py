/*링크 : https://programmers.co.kr/learn/courses/30/lessons/12933 */

def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    
    return int("".join(n))

'''
1. 정수n을 str로 변환->list로 변환
2. list n을 sort()함수로 내림차순 정렬(reverse=True)
3. list->string으로 ""join()변환하고 int로 변환해 return
'''