while True:
    #세 변의 길이 입력받기
    sides = list(map(int,input().split()))
    
    # 종료 조건 : 0 0 0 이 입력되면 종료
    if sides == [0,0,0]:
        break
    #세 변을 오름차순으로 정렬
    sides.sort()
    
    #피타고라스 정리
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")
    