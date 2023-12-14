def solution(arr):
    X = []     # 아무 원소도 들어있지 않은 빈 배열 선언
    
    for num in arr:
        X.extend([num]* num)
    return X



'''
#오답노트 
Q. append가 아니라 extend를 사용한 이유
- append: 리스트에 하나의 원소를 추가할 때 사용
ex) X.append(num) -> 리스트 X의 끝에 'num' 이라는 하나의 원소 추가 
- extend: 리스트에 다른 리스트의 모든 원소를 추가할 때 사용
ex) X.extend([num]*num) -> 리스트 X의 끝에 'num'이라는 원소를 'num'번 반복한 리스트를 추가

위 문제는 각 원소의 값에 해당하는 숫자만큼 반복된 리스트를 추가해야하므로, 
'extend'를 사용하여 한번에 여러 개의 원소를 추가함
(append를 사용하면 각 반복마다 하나의 원소만 추가될 것)
'''
