def solution(n):
    return [x for x in range(n+1) if x%2]


'''
range에서 스텝값을 생략하고 x%2를 사용해
나머지가 있을 때(=홀수)를 출력
# range(시작,끝,스텝)

다른 풀이
def solution(n):
    return [ i for i in range(1,n+1,2)]
-> 1이상 n+1미만 범위에서 2씩 건너뜀
'''
