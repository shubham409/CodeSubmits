n,m=list(map(int,input().split()))
p=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
i=p.index(n)
if p[i+1]==m:
    print('YES')
else:
    print('NO')