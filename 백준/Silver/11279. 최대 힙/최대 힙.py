import sys, heapq
heap=[]

for i in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip()) * -1
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)*-1)
    else:
        heapq.heappush(heap,n)
        

