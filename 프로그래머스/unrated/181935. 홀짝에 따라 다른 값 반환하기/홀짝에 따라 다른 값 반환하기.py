def solution(n):
    return sum([n**2 for n in range(2, n+1, 2)]) if n % 2 == 0 else sum([n for n in range(1, n+1, 2)])