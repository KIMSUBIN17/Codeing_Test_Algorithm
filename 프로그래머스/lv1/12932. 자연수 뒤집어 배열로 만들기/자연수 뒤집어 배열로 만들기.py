def solution(n):
    answer = []
    n = str(n)  #정수n -> 문자열n
    for i in n[::-1]:
        answer.append(int(i))
    return answer