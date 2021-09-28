/* 링크 : https://programmers.co.kr/learn/courses/30/lessons/72410 */

def solution(new_id):
    answer = ''
    
    #step1:모든 대문자를 소문자로
    new_id = new_id.lower()
    
    #step2:소문자,숫자,빼기,밑줄,마침표 제외 모든 문자 제거
    for c in new_id:
        if c.isloswer() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
            
    #step3:마침표 2번 이상 -> 하나로
    while '..' in answer:
        answer = answer.replace('..','.')
    
    #step4:양 끝 마침표 제거
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:] 
        else: 
            '.'
        
    if answer[-1] == '.':
        answer = answer[:-1]
        
    #step5:빈 문자열이라면 a 대입
    if len(answer) == 0:
        answer = 'a'
        
    #step6:길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #step7:길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer



'''
#풀이
1. new_id.lower() : 모든 알파벳을 소문자로 변경
cf) upper() : 모든 알파벳을 대문자로

2. islower() : 문자열이 모두 소문자인 경우 True, 하나라도 아니라면 False
isdigit() : 문자열이 모두 숫자인 경우 True, 하나라도 아니라면 False
in ["-","_","."] : 여러 조건 있을 때 in / cf: not in도 사용가능

3.answer.replace('..','.') : 문자열에서 replace함수는 문자열의 값을 변경
..를 . 로 변경하게 됨. answer 안에 ..이 없을 때까지 반복함

4. 문자열 인덱스 사용해 첫번째 인덱스[0]의 값이 "."인 경우 슬라이싱으로 [1:] 두번째부터의 값이 입력되도록 함
이때 answer의 문자열이 1개라면 index out of range문제가 생기므로 길이가 2이상일때 이를 사용한다는 조건 추가. 문자열 길이가 1개인 경우는 "."로 따로 정의
[:-1] 인덱스를 사용하는 경우 : 끝 값

5. 빈 문자열인 경우. 
if answer == "":
    answer = "a"로도 표현 가능
(빈문자열 : "")

6. 슬라이싱을 이용해 15자리까지로 변경. 이때 끝값이 "."이 되면 이를 제거함

7. answer의 값이 3미만인 경우 answer[-1]을 사용해 마지막 값을 계속해서 덧붙임
answer[-1] : 마지막 값



문제 설명
카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어, 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다. "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
다음은 카카오 아이디의 규칙입니다.

아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
"네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
신규 유저가 입력한 아이디가 new_id 라고 한다면,

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.



#다른사람풀이(정규식 사용)

import re

def solution(new_id):
    answer = new_id
    answer = answer.lower()
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    answer = re.sub('\.+', '.', answer)
    answer = re.sub('^[.]|[.]$', '', answer)
    answer = 'a' if len(answer) == 0 else answer[:15]
    answer = re.sub('^[.]|[.]$', '', answer)
    answer = answer if len(answer) > 2 else st + "".join([answer[-1] for i in range(3-len(answer))])
    return answer

import re

def solution(new_id):
    answer = ''
    # 1단계 & 2단계 : 소문자 치환
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    # 3단계 : 마침표 2번 이상 > 하나로
    answer = re.sub('\.\.+', '.', answer)
    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)
    # 5단계 : 빈 문자열이면 a 대입
    if answer == '':
        answer = 'a'
    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])
    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1:]
    return answer


#다른 풀이 설명(정규표현식)
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
- new_id.lower() : 소문자로 바꿔준다.

2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
- 소문자(a-z), 숫자(\d), 빼기(\-), 밑줄(\-), 마침표(\.)를 제외한(대괄호 [] 맨 앞에 ^를 붙여준다.) 모든 문자 제거
- 이때 빼기, 밑줄, 마침표 앞에 오는 \는 이스케이프이다. 
- 정규표현식이 일치하면 '' 빈 문자로 치환(sub)하여 문자를 제거한다.

3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
- 마침표가 2번 이상 (\.\.+)인 것을 마침표로 치환(sub)

4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
- 마침표가 처음(^\.)이나 끝(\.$)

5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
- 빈 문자열('')이면 'a' 대입

6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다. 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
- 첫 15개의 문자만 사용 = answer[0:15]
- 맨 끝에 위치한 마침표('\.$')

7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
- 길이가 3이 될 때까지 (while len(answer) < 3) 마지막 문자 (answer[-1:])를 맨 끝에 붙여준다.
- 문자열 + 문자열 를 하면 순서대로 문자열이 합쳐지기 때문에 answer += answer[-1:] 를 해주었다.


'''