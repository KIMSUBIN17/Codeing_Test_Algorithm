s = input()
#맨 앞 글자를 뺀 문자열을 저장시킬 list 선언
#입력받은 input() 문자열의 길이만큼 반복시키는 반복문 생성
answer = []

#맨 앞글자 제외하고 나머지 뒤의 문자열 append_i부터 끝까지
for i in range(len(s)):
    answer.append(s[i:])
    
answer.sort()

for i in answer:
    print(i)