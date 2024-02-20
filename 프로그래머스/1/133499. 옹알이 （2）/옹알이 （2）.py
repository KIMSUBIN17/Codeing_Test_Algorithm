def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    #babbling의 단어 하나씩 순회
    for word in babbling:
        #단어 하나씩 순회하면서 발음가능한 can 조합 확인
        for c in can:
         # 말할수있는 단어(can배열)중에서 글자가 연속으로 나오지 않으면 공백으로 대체(c*2가 can에 존재하는지 확인하고, 공백으로 대체)

            # 단어에서 발음 가능한 조합이 연속해서 나오지않으면 해당 부분 공백으로 대체
            if c * 2 not in word:
                word = word.replace(c, ' ')
                #단어가 공백으로만 이루어져 있다면, 조건을 만족하는 단어로 판단해 answer를 1 증가시킴
        if word.isspace():
            answer += 1
                
    return answer


'''
참고링크 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%98%B9%EC%95%8C%EC%9D%B42-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python


#해설
연속으로 발음할 수 없다 -> c*2가 존재하지 않을때만 공백으로 대체 -> 발음할 수 있는 단어들을 공백으로 대체하면 대체 후 남는 문자들이 존재하면 해당 단어는 발음할 수 없는 단어


첫 번째 반복에서 c에 'aya'가 할당되고, 'aya'는 can 리스트에 있는 발음 가능한 조합 중 하나이므로 따라서 첫 번째 반복에서는 'aya'를 확인. 만약 'aya'가 연속해서 두 번 등장하지 않는다면 공백으로 처리(=발음가능하다 판단) 그런 다음 두 번째 반복부터는 'ye', 'woo', 'ma'를 차례대로 확인하여 동일한 작업을 반복
'''