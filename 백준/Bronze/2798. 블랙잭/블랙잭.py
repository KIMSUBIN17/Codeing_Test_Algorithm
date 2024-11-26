from itertools import combinations

n, m = map(int,input().split())
cards = list(map(int, input().split()))

# 변수 초기화
max_sum = 0

# 카드의 모든 3장에 대한 조합 
for comb in combinations(cards, 3):
    current_sum = sum(comb)
    #각 조합의 합이 M을 넘지않으면 최댓값 갱신
    if current_sum <= m:
        max_sum = max(max_sum, current_sum)
        
print(max_sum)


'''
브루트포스는 O(n^3) 로 효율적이지 않을 수도 있지만, 
N=100의 조건에서는 약 161,700개의 조합을 계산해야하지만 해당 문제에서는 충분히 처리 가능할듯함

n,m 입력받는 부분에서 map()을 사용하지 않으면, 
입력받은 데이터를 문자열의 상태로 처리하게 되어 타입 에러가 발생함
(정수와 문자열은 서로 비교할 수 없음)

--> map()함수는 숫자 변환이 필요한 곳에서 거의 필수적으로 사용한다고 생각하면 됨
ex1) 숫자 여러개 입력받을 때
n,m = map(int,input().split())
ex2) 숫자 리스트 입력
lst = list(map(int,input().split()))


* combinations
- itertools.combinations(iterable, r)
- 주어진 iterable에서 길이 r의 모든 조합을 생성
- 중복허용X, 순서 상관X

Q. range를 쓰지않은 이유
A. range는 숫자 범위를 생성하는데 주로 쓰이며, 조합 생성을 위해서는
직접 i,j,k를 직접 관리해서 중첩 for문을 작성해야하는데
바로 combinations을 하면 N개의 원소에서 R개의 조합을 만들때 r만 변경해서 바로 처리가 가능함


'''