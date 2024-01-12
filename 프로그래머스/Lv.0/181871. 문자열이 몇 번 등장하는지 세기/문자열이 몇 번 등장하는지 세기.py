def solution(myString, pat):
    count = 0
    #myString에서 pat이 등장하는 횟수 세기
    for i in range(len(myString)):
     # 현재 부분 문자열이 pat과 일치하는지 확인해서 일치하면 count를 증가
        if myString[i:len(pat)+i] == pat:
            count += 1
    return count