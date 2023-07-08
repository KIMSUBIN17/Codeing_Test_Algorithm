# 다시 풀어보기
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

'''
n과의 거리의 절대값 =  abs(x-n)에 대해 정렬하고,
abs(n-x)가 같으면 n-x가 큰 값을 먼저 정렬


#다른사람의 풀이
def solution(numlist,n):
    numlist = [(abs(n-num), -num) for num in numlist]
    #첫번재 요소를기준으로 오름차순 정렬 and 두번째 요소 기준으로 내림차순 정렬
    numlist.sort()
    #두번째 요소만  리턴
    return [-num for _, num in numlist]
'''