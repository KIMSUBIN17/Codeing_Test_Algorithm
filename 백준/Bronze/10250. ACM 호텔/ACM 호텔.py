T = int(input())

for i in range(T):
    #h = 각 호텔의 층 수, w = 각 층의 방 수, n = 몇 
    h,w,n = map(int,input().split())
    
    floor = n % h 
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)
    
    

'''
손님의 번호가 H가 넘어가면 N % H (N번째 손님을 층수로 나눈 나머지)만큼의 층에 머무르고,
(N/H)+1 만큼 엘리베이터에서 떨어진 곳
'''