#두 개의 자연수 입력받기
a,b = map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b = b,a % b
    return a
def lcm(a,b):
    return a * b //gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))