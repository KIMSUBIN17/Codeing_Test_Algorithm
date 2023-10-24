def solution(score):
    answer = []         #각 평균값의 등수
    avg = [sum(i)/2 for i in score]
    #평균이 큰 값부터 내림차순으로 정렬
    sort_avg = sorted(avg, reverse= True)
    
    for i in avg:
        #index는 0부터 시작하므로, 등수 표현위해 각 index값에 1을 더함
        answer.append(sort_avg.index(i)+1)
    return answer


'''
참고 링크 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%93%B1%EC%88%98-%EB%A7%A4%EA%B8%B0%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
'''