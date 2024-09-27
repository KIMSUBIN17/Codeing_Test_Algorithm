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