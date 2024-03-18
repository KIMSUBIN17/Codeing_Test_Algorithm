def solution(intStrs, k, s, l):
    answer = []
    
    for string in intStrs:
        #시작 인덱스 s부터 l까지의 부분 문자열을 잘라내고
        # 정수로 변환해서 k와 값을 비교하여, 변환한 정수가 k보다 크면 answer로 반환
        substring = string[s:s+l]

        num = int(substring)
        
        if num > k:
            answer.append(num)
            
        #print(substring)
        #print(string)
        
    return answer
