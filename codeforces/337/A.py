f=lambda:map(int,input().split())
n,m=f()
a=sorted(f())
print(min(a[i+n-1]-a[i] for i in range(m-n+1)))