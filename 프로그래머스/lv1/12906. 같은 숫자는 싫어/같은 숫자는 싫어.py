def solution(arr):
    answer = []
    for i in range(len(arr)): # [1,1,3,3,8,1,1] --> 7, 0123456
        if i == 0:    #배열의 첫번째 값
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
    
    
'''
i값과 i+1값을 비교하면 배열의 마지막을 확인할 경우, 배열 밖의 값과 비교를 할 수 없으므로 out of range오류 발생
--> i값과 i-1값 비교함
-->  첫번째 값은 이전값과 비교할 수 없으므로 일단 배열에 넣음
이전값과 현재값 비교해 같지않으면 배열에 추가

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
            
    return answer

'''