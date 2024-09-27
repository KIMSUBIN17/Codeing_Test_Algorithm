import sys

# 학생 수 입력받기
n = int(input())
students = []    #학생정보 저장할 리스트 

#학생 정보 입력
for _ in range(n):
    name, korean, english, math = input().split()
    students.append((name,int(korean),int(english), int(math)))        #(이름,점수)튜플로 저장
    
#정렬
students.sort(key = lambda x: (-x[1], x[2],-x[3], x[0]))

#결과 출력
for student in students:
    print(student[0])        #각 학생 이름만 출력


'''
* 인덱스를 사용하지 않을 때: for _ in range(n)를 사용.
단순히 반복만 필요할 때.
--> 단순 반복만 필요
* 인덱스를 활용할 때: for i in range(n)를 사용.
인덱스 값이 필요하거나, 그 값에 따라 다른 동작을 할 때.
--> 루프 내에서 인덱스의 값을 사용해야 하거나, 인덱스에 따라 동작을 달리해야 할 때 i와 같은 변수를 사용

'''
