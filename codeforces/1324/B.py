for _ in range(int(input())):
    n = int(input())
    ans = "NO"
    a = list(map(int,input().split()))
    for i in range(len(a)-2):
        if a[i] in a[i+2:]:
            ans = "YES"
            break
    print(ans)