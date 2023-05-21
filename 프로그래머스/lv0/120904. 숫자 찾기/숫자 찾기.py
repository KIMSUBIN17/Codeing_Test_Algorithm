def solution(num, k):
    answer = 0
    a = str(num)
    b = str(k)
    
    for i in a:
        answer += 1
        if b == i:
            return answer
    return -1

'''
# 다른 사람의 풀이
def solution(num,k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
    
# find()
- 찾는 문자가 없으면 -1 출력
- 문자열을 찾을 수 있는 변수는 문자열만 사용 가능
- 리스트, 튜플, 딕셔너리 자료형에서는 사용 불가(에러)

# index()
- 문자열, 리스트, 튜플자료형에서 사용 가능 / 딕셔너리 자료형 사용 불가



'''

