def solution(array):
    answer = ""
    for i in array:
        answer += str(i)
    return answer.count("7")

'''
array의 값을 str 문자열로 변환하고, count()함수 사용해 7의 개수를 구함

'''