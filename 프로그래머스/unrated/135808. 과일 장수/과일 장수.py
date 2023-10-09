def solution(k, m, score):
    answer = 0      #이익
    #내림차순 정렬 
    #최대이익 = 각 상자의 점수들도 최대이도록 내림차순으로 큰 값부터 정렬해야함
    score.sort(reverse = True)  
    #m개씩 슬라이싱=한상자에 담기는사과의 점수
    for i in range(0,len(score),m):
        #슬라이싱한 길이가 m인지 확인(상자에는 m개씩 담겨야함)
        if len(score[i:i+m]) == m:
            #각 상자에서 가장 낮은 점수 * m = 해당 상자의 가격
            #answer = 각 상자의 점수를 모두 더함
            answer += min(score[i:i+m]) * m
    return answer


'''
참고링크 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%BC%EC%9D%BC-%EC%9E%A5%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
'''