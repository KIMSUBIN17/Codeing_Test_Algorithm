def solution(array):
    while len(array) !=0:
        for i,a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a    
    return -1

'''
#다른 사람의 풀이 해설 정리

1. array의 길이가 0이 아닐때(=array에 요소가 남아있을때)까지 set(array)의 요소(a)를 지워가는 것을 반복함
    
#enumerate()함수
enumerate 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌
for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있음
(ex. for a,b in enumerate(['가','나']))

1. set()을 사용해 중복 제거
set()은 순서가 없고 고유한 값을 가지므로 값의 중복이 불가능
--> 순서가 없으므로 리스트나 튜플처럼 인덱싱도 불가능! / 집합처리할 때 많이 사용
2. 중복 제거된 set 상태에서 입력받은 array에서 값이 없어질때까지 한번씩 지움
3. i=0이면 모두 지워지고 하나의 값만 남았으므로 그 값을 리턴 / i가 0이 아니라면 -1 리턴

'''