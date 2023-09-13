def solution(n):
    arr = list(str(n))
    arr.reverse()
    
    return list(map(int, arr))

'''
def solution(n):
    answer = []
    n = str(n)  #정수n -> 문자열n
    for i in n[::-1]:
        answer.append(int(i))
    return answer
    
* reversed()함수 : 리스트의 자료형이 아님 
--> list()통해 변환필요함
'''
