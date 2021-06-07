n = int(input())

for i in range(n):
    c, s = map(int, input().split())
    a = s//c
    b = s % c
    print((a**2)*(c-b)+b*(a+1)**2)
