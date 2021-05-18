for _ in range(int(input())):
    n=int(input())
    l=[1]*2+[0]*(n-2)
    for i in range(n):
        ans=l[n-i:]+l[:n-i]
        print(*ans)