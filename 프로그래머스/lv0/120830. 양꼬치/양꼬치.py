def solution(n, k):
    drink = n // 10
    answer = 12000*n + 2000*(k-drink)
    return answer