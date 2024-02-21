-- 2024.02.21
def solution(arr):
    answer = []
    
    answer = [arr[0]]   # 첫번째 원소는 무조건 포함되어야함
    #첫번째 원소 이후 두번째 원소부터 끝까지 순회
    for num in arr[1:]:
        if num != answer[-1]:   #순회하는 num값과 answer의 이전 원소가 다르면 추가(다르면 중복되지 않으므로 조건 충족)
            answer.append(num)
        else:
            continue
        
    return answer

'''
#오답노트 
Q. set을 사용할수는 없는가 ? 
A. set함수로 중복 숫자 제거는 가능하나, set은 배열의 순서 유지 보장이 안되기 때문에 문제의 요구사항을 충족할 수 없으므로 불가
'''

'''
#다른풀이1
def solution(arr):
    answer = [] # 숫자 담을 리스트
    last = -1 # 마지막으로 넣었던 숫자 / arr요소들이 0이상의 정수이기때문에 -1로 선언
    
    for i in arr:
        if i == last: # 현재 숫자 i가 마지막으로 넣은 숫자와 같으면
            continue # 패스
        answer.append(i) # 같지않으면 i를 answer에 추가
        last = i #마지막으로 담은 숫자를 i에 넣음
    return answer
    
    

#다른풀이2
def solution(arr):
    answer = []
    for i in range(len(arr)): # [1,1,3,3,8,1,1] --> 7, 0123456
        if i == 0:    #배열의 첫번째 값
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
    
    
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
