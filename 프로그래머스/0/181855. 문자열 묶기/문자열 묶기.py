def solution(strArr):
    tmp = []    #각 길이별 문자열의 갯수를 저장할 빈 리스트 선언
    #문자열 배열 strArr에 대해 각 문자열의 길이 계산해 리스트에 저장
    answer = [len(i) for i in strArr]
    #중복제거해 리스트에 있는 고유한 길이들을 순회함
    for i in set(answer):
    #각 고유한 길이 i에 대해 해당 길이가 answer 리스트에 몇번 등장하는지 세어 tmp에 추가(각 길이별로 몇 개의 문자열이 있는지 tmp리스트에 저장)
        tmp.append(answer.count(i))
    #리스트에서 가장 큰 값 반환(=가장 많은 개수를 가진 길이)
    return max(tmp)