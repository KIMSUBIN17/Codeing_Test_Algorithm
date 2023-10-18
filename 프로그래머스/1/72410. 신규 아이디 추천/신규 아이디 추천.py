def solution(new_id):
    answer = ''
    
    #1. 대문자-> 소문자 치환
    new_id = new_id.lower()
    
    #2. 소문자,숫자,빼기,밑줄,마침표 제외 모든 문자 제거
    for c in new_id:
        if c.islower() or c.isdigit() or c in ['-','_','.']:
            answer += c
            
    #3. 마침표 2번 이상 -> 하나로 치환
    while '..' in answer:
        answer = answer.replace('..','.')

    
    #4. 양 끝 마침표 제거 
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            '.'
    
    if answer[-1] == '.':
        answer = answer[:-1]
        
   #5. 빈 문자열이면 a 대입
    if len(answer) == 0:
        answer = 'a'
    #6. 길이가 16자 이상이면 1~15만 남기기 & 맨 끝 마침표 제거
    if len(answer)>15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7. 길이가 3이 될때까지 반복해서 끝에 붙이기 
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer