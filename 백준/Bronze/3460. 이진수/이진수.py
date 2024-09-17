t = int(input())            #테스트케이스 수 입력

for i in range(t):
    ans = []
    n = int(input())        #숫자 n 입력
    
    while n>= 1:           #숫자 n을 이진수로 변환
        ans.append(n % 2)
        n = n //2
        
    for j in range(len(ans)):
        if ans[j]== 1:            #1일 경우 그 위치 j를 출력
            print(j, end = " ")





'''''''''''''''''''''''''''''''
#다른 풀이
'''
- enumerate 사용해 index와 value에 동시에 접근 가능
- 숫자 n을 이진수 변환 라이브러리(bin)를 사용해 풀이
2진수 변환시 0bXXXXX와 같이0b로 시작하므로 0b제외하고 숫자만 뽑기위해
[2:] 인덱싱 처리(인덱싱 처리 했으므로 문자열임0

'''
t = int(input())

for _ in range(t):
    n = int(input())

    n = bin(n)   # 앞에 0b가 포함되어 나타남(문자열)
    n = n[2:]    # 13 -> 1101


    for idx, val in enumerate(n[::-1]):
        if val == '1':
            print(idx, end=" ")
