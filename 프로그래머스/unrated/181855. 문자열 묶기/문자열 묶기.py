def solution(strArr):
    #strArr에 있는 각 문자열의 길이를 측정하여 answer에 저장
    answer = [len(i) for i in strArr]
    tmp = []
    #set을 사용해 중복제거한 고유 길이 값들을 대상으로 for문 수행
    for i in set(answer):
        #각 길이 i에 대해 answer리스트에서 해당 길이의 갯수를 세어 tmp에 추가함
        tmp.append(answer.count(i))
    #tmp리스트의 값 중 가장 큰 값을 리턴 = answer리스트에서 가장 많이 등장한 길이의 갯수를 나타냄 
    return max(tmp)