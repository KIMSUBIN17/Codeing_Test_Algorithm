def solution(t, p):
    answer = 0      # 결과 저장할 변수 
    p_len = len(p)  # 문자열 p 길이를 p_len변수에 저장
    
    # 문자열 t 순화하면서 p와 길이가 같은 부분 문자열 추출
    for i in range(len(t) - p_len + 1):
        #i부터 추출하려는 p_len의 길이만큼 추출해 비교
        if int(t[i:i+p_len]) <= int(p):
            answer += 1   
    
    return answer


'''
#오답노트
- for i in range(len(t)):   >> 오답
-> 문자열 t를 순회할 때, 부분 문자열의 범위를 잘못 선택했기 때문
현재 코드에서는 t[i:i+p_len]로 부분 문자열을 추출하고 있지만, 
그냥 len(t)로 하면 마지막 부분에 대한 검사가 안됨(=마지막 부분 문자열이 누락됨)

*range()함수 : 
range(n) --> n-1까지의 숫자 생성 !!!!!(주의)

ex. t="3141592", p="271" 부분문자열 추출 시 
314 (0부터 3까지)
141 (1부터 4까지)
415 (2부터 5까지)
159 (3부터 6까지)
592 (4부터 7까지)
현재 len(t)로 순회하면 마지막 부분 문자열 592가 누락됨
마지막 부분 문자열까지 순회할 수 있도록 len(t)-p_len+1까지 순회되어야함


# 2차 오류
- for i in range(len(t)+ 1):
>> ValueError: invalid literal for int() with base 10: '' 오류발생
--> 범위가 너무 커짐; t문자열의 모든 부분 문자열을 고려하게 되는데 문제의 요구사항과 맞지않음

'''