for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split(' ')))
    for i in range(n-1,-1,-1):
        if a[i]+i<n: a[i]+=a[a[i]+i]
    print(max(a))