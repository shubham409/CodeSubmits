a,b,c=map(int,input().split())
print(min(a+b+c,a+b<<1,a+c<<1,b+c<<1))