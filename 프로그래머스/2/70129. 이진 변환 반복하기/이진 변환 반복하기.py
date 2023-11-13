def solution(s):
    cnt = 0 #이진 변환 횟수 
    zerocnt = 0     #제거된 0의 갯수
    
    #1이 남을때까지 반복 
    while True:
        if s == '1':
            break
        
        zerocnt += s.count("0")     #문자열의 0의 갯수 세기
        s = s.replace("0",'')      # 0 -> 공백 변환
        # 이진 문자열 앞자리에 포함된 "0b"삭제하기위해
        s= bin(len(s))[2:]  # 2진수변환_이진문자열 앞에 "0b" 삭제
        
        cnt += 1
        
    return [cnt, zerocnt]
    
    #answer = [cnt, zerocnt]
    #return answer
    
    
'''
1. 문자열 s가 들어왔을때 0의 갯수 세고, 0을 제거함
2. 제거된 문자열 s의 길이를 2진수로 변환후, 위 작업을 1이 남을때까지 반복
3. s.count(0) --> 문자열 s의 0의 갯수를 세고, zerocnt 변수에 저장
4. s.replace("0",'') --> 문자열 s의0을 공백으로 치환
5. bin() --> 이진수 변환
6. bin(len(s)) --> 문자열 s의 길이를 이진 문자열로 변환 후 [2:] 슬라이싱 하여 이진 문자열 앞자리에 붙는 "0b"삭제

참고링크 : https://siloam72761.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%9D%B4%EC%A7%84-%EB%B3%80%ED%99%98-%EB%B0%98%EB%B3%B5%ED%95%98%EA%B8%B0
'''