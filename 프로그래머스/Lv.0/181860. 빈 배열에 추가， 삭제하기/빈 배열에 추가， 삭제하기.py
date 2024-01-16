def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
        if flag[i]:
            #flag가 true이면 arr[i]를 arr[i] * 2번 추가
            answer += [arr[i]] * (arr[i] * 2)
        else:
            #flag가 flase이면 X에서 마지막 arr[i]개이 원소 제거
            answer = answer[:-arr[i]]
            
    return answer