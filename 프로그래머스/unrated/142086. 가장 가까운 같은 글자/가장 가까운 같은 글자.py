def solution(s):
    answer = []
    dic = {}
    #enumerate : 인덱스와 인덱스의 원소가 튜플 형태로 담겨 저장
    #문자열s를 인덱스idx와 함께 돌아 확인한 문자와 인덱스를 함께 저장
    for idx, alpha in enumerate(list(s)):
        if alpha not in dic:
            answer.append(-1)
            dic[alpha] = idx
        else:
            answer.append(idx-dic[alpha])
            dic[alpha] = idx
    
    return answer