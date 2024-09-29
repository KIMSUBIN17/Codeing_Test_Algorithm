#입력받기_모두 대문자로 변환(대소문자 구분없이 사용하도록)
word = input().upper()
#입력된 단어의 중복된 알파벳을 제거-고유한 알파벳만 남김
#set()->중복제거 / list()리스트로 변환
word_list = list(set(word))

cnt = []        #알파벳의 등장 횟수를 저장할 빈 리스트 cnt를 초기화
for i in word_list:
    count = word.count    #word.count(i)-->i가 몇번 등장하는지 세는 함수
    cnt.append(count(i))
    
if cnt.count(max(cnt))  > 1:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))])        
    #최대값의 인덱스 반환
    #그 인덱스에 해당하는 알파벳을 word_list에서 찾아 출력