#난쟁이들의 키 입력받기
h = [int(input()) for _ in range(9)]

#난쟁이들의 전체 키 합
tot_h = sum(h)

# 두 명의 난쟁이를 찾기
for i in range(9):
    for j in range(i+1, 9):
        #두 난쟁이들을 제외한 나머지 7명의 합이 100이 되는 경우
        if tot_h - h[i] - h[j] == 100:
            pick_h = [h[k] for k in range(9) if k != i and k != j]
            pick_h.sort()    #오름차순 정렬
            
            print("\n".join(map(str,pick_h)))
            exit()
            
            
'''
#이중for문 해석
h[k] for k in range(9)
- 0~8까지 총9명에 대한 리스트 생성
- h[k]는 난쟁이들의 키가 저장된 h리스트에서 k번째 난쟁이의 키를 가져옴
- if k!= i and k!=j 에서 i,j는 선택한 두 명의 난쟁이
i,j번째 난쟁이를  제외한 나머지 난쟁이들을 리스트에 포함하여, 
나머지 7명의 난쟁이들의 키만 pick_h[]리스트에 들어감
만약 i = 2이고 j = 5라고 가정하면 
h 리스트에서 2번째와 5번째 난쟁이는 제외하고, 
나머지 0, 1, 3, 4, 6, 7, 8번째 난쟁이들의 키만 새롭게 pick_h 리스트에 담기는 것
'''            
