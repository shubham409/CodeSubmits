n,m=map(int,input().split())
d={}
for _ in range(m):
    a,b=input().split()
    d[a]=a if len(a)<=len(b) else b
for i in input().split():
    print(d[i],end=' ')