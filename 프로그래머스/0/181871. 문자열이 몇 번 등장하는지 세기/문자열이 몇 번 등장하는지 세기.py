def solution(myString, pat):
    count = 0
    #myString에서 pat이 등장하는 횟수 세기
    for i in range(len(myString)):
     # 현재 부분 문자열이 pat과 일치하는지 확인해서 일치하면 count를 증가
        if myString[i:len(pat)+i] == pat:
            count += 1
    return count

'''
문자열을 탐색하여 패턴이 등장하는 횟수를 세는데 사용
현재 인덱스에서부터 패턴의 길이만큼의 부분 문자열을 추출하여
이 부분 문자열이 주어진 패턴과 일치하는지 확인하고
일치하면 count를 증가시킴

#주의점
myString의 길이가 n이고 pat의 길이가 m인경우,
시간복잡도가 O(n*m)가 되기때문에 입력이 크면 성능에 영향을 미칠 수 있으므로 다른방법도 고안해볼 것
'''