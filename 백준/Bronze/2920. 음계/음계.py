a = list(map(int, input().split()))
 
if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')
    
'''
sorted()함수 사용해 오름차/내림차순으로 정렬된 값을 반환
(리스트의 원본값은 그대로 유지)
'''