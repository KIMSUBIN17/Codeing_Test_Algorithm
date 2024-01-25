#풀이1. Brute force
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):    #앞의 수
        for j in range(i+1, len(prices)):   #뒤의 수
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer