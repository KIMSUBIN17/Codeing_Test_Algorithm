H, M = map(int, input().split())

#분(M)이 45분 이상이라면 M-45가능
if M >= 45:
    M -= 45
#분(M)이 45보다 작으면, -45했을때 음수가 나오고 전날 시간으로 돌아가므로 음수를 보정하기 위해 60분 더하고 시간(H)에서 1시간을 뺌
else:
    M += 60-45
    if H == 0:        #시간이 0시일 때는 하루의 맨 마지막 시간인 23시로 돌아감
        H = 23
    else:
        H -= 1
        
print(H,M)