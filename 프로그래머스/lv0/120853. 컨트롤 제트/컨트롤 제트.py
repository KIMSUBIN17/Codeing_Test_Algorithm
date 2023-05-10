def solution(s):
    answer = []
    
    for num in s.split():
        if num == "Z":
            answer.pop()
            continue
        answer.append(int(num))
    return sum(answer)


'''
참고 풀이
https://somjang.tistory.com/entry/Programmers-%EC%BB%A8%ED%8A%B8%EB%A1%A4-%EC%A0%9C%ED%8A%B8-Python

'''