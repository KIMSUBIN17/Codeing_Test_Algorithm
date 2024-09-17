n = int(input())

words = [str(input()) for i in range(n)]

#중복값 제거 위해 set함수 사용 후 set한 words를 리스트에 담음
words = list(set(words))    
words.sort()        #문제조건에 따라 사전순 정렬 먼저 수행
words.sort(key=len)        #길이순 정렬

for i in words:
    print(i)