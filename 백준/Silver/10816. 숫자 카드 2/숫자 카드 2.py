# 입력
n = int(input())     # 상근이가 가진 숫자 카드의 개수
cards = list(map(int, input().split()))        # 상근이가 가진 숫자 카드들
m = int(input())            # 구해야 할 숫자 카드의 개수
targets = list(map(int, input().split()))        # 구해야 할 숫자 카드들

# 숫자 카드를 카운팅_딕셔너리를 사용해 카운팅하기 
card_cnt = {}
for card in cards:
    if card in card_cnt:
        card_cnt[card] += 1
    else:
        card_cnt[card] = 1

# 결과 출력
result = [card_cnt.get(target,0) for target in targets]
print(' '.join(map(str,result)))


'''
Counter사용하면 딕셔너리 직접 구축하지 않아도 됨
>>풀이 
from collections import Counter


n = int(input()) 
cards = list(map(int, input().split()))  
m = int(input())  
targets = list(map(int, input().split())) 


card_count = Counter(cards)


result = [card_count[target] for target in targets]
print(' '.join(map(str, result)))
'''
            
