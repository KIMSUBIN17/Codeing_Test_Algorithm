# 유클리드 호제법 이용_두수 곱한것을 그 두수의 최대 공약수로 나누면 최소공배수가 됨
def gcd(n,m):
    mod = m % n
    if mod != 0:
        m,n = n, mod
        return gcd(n,m)
    else:
        return n    

def solution(n, m):
    answer = [gcd(n,m), n*m / gcd(n,m)]
    return answer