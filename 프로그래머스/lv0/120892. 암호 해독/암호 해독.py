def solution(cipher, code):
    answer = ''
    for i  in range(code,len(cipher)+1):
        #code(배수의 시작)부터 cipher배열의 끝까지 반복
        if i % code == 0: 
            # code로 나누었을때 0 -> 배수
            print(i)
            answer+=cipher[i-1]
            #배열은 인덱스0부터 시작하므로 -1해줘야함
    
    
    return answer

'''
#놓쳤던 것
4,8,12,16,20번째
-> 인덱스로 치면 3,7,11,15,19번째임

#다른 사람 풀이
#1.range(start,stop,step) 사용
start부터 stop까지 step만큼 !
배열이므로 code-1 해야함

def solution(cipher,code):
    answer = ''
    for i in range(code-1,len(cipher),code):
    answer+=cipher[i]
    return answer
    
    
#2. 슬라이싱 사용
def solution(cipher,code):
    answer = cipher[code-1::code]
    return answer
    
'''