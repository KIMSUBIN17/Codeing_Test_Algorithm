def solution(k, score):
    answer = []
    top_list = []
    
    for i in score:
        #점수list에서 꺼낸 값을 리스트에 append
        top_list.append(i)
        #내림차순 정렬 후 상위k개만 리스트에 남김
        top_list = sorted(top_list,reverse=True)[:k]
        #상위k개만 남은 리스트에서 가장 작은값을 answer리스트에 append
        answer.append(min(top_list))
    return answer

'''
참고링크 
https://somjang.tistory.com/entry/Programmers-%EB%AA%85%EC%98%88%EC%9D%98-%EC%A0%84%EB%8B%B9-1-Python
'''