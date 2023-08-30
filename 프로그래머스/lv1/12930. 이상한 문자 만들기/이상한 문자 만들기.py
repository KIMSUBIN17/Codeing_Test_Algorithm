def solution(s):
    answer = ''		# 빈 문자열 선언
    idx = 0		# 인덱스 선언
    
    for val in s:	# 문자열 s를 돌면서
        if val.isalpha():	# 지금 보는 문자가 알파벳이면
            if idx%2 == 0: # 현재 짝수 인덱스라면
                answer += val.upper()	# 대문자로 변환
            else:	# 홀수 인덱스라면
                answer += val.lower()	# 소문자로 변환
            idx += 1	# 인덱스 증가
        else:	# 지금 보는 문자가 공백문자라면
            answer += ' '	# 공백 추가
            idx = 0	# 인덱스 0으로 초기화
                
    return answer


'''
#해설
문자열 전체의 짝/홀수 인덱스(X)
단어(공백기준으로 split한 상태)별로의 짝/홀수 인덱스(O)

참고링크 : https://velog.io/@mauserne/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A0%88%EB%B2%A8-1-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4python-1


'''