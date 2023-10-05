def solution(cards1, cards2, goal):
    for i in goal:
        #goal을 돌면서 해당 요소가 cards1이나 cards2의 0번째 요소와 같은지 비교하고, 같은게 있으면 꺼냄
        if len(cards1) and i == cards1[0]:
            cards1.pop(0)
        elif len(cards2) and i == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'


'''
* 0번인덱스와 비교하는 이유 
cards1[0] 또는 cards2[0]에 접근하려면 두 리스트가 빈 리스트면 안됨
if i == cards1[0]만 작성하면 cards1에 요소가 하나도 없을때 indexError발생할 수 있음
'''

'''
참고링크 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B9%B4%EB%93%9C-%EB%AD%89%EC%B9%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
'''