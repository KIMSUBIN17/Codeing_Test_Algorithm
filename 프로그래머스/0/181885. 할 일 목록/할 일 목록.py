def solution(todo_list, finished):
    unfinished = []     #아직 마치지 못한 일들을 저장할 리스트
    
    #todo_list와 finished 배열을 돌면서 아직 마치지 못한 일들을 찾아서 unfinished 리스트에 추가 
    for i in range(len(todo_list)):
        if not finished[i]:
            unfinished.append(todo_list[i])
            
    return unfinished



'''
# 다른풀이
def solution(todo_list, finished):
    answer = []
    for a,b in zip(todo_list, finished):
        if b == False:      #b가 False면 아직 마치지못한것
            answer.append(a)
    return answer


- zip() 함수
반복문을 수행할 때, 두 개의 리스트의 값을 각각 가져와야할 때 유용
'''
