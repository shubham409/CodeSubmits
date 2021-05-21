n,x=map(int,input().split())
m=0
for case in range(n):
    d=int(''.join((input().split(' '))))
    if x+d<0:
        m+=1
    else:
        x+=d
print(x,m)