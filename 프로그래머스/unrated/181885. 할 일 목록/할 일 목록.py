def solution(todo_list, finished):
    answer = []
    for a,b in zip(todo_list, finished):
        if b == False:      #b가 False면 아직 마치지못한것
            answer.append(a)
    return answer

'''
zip() 함수
반복문을 수행할 때, 두 개의 리스트의 값을 각각 가져와야할 때 유용
'''