a, b = map(int, input().strip().split(' '))
#input()함수로 입력받고
#.strip() 메소드로 문자열의 시작과 끝의 공백문자 제거하고
#.split(' ') 메소드로 공백문자를 기준으로 문자열 가름
#map()함수 : 갈라낸 문자열을 하나씩 바다 int함수를 돌려서 뱉어냄

for _ in range(b):   #변수필요없으면 변수자리에 _ 쓰기
    print('*'*a)        #*을 a번찍기
    
    
'''
n,m = map(int, input().strip().split(' '))

for i in range(1, m+1):
    print("*" * n)

'''