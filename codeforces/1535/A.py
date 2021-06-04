def fun(ls):
    a,b,c,d=ls
    min1=min(a,b)
    min2=min(c,d)
    max1=max(a,b)
    max2=max(c,d)
    if(min1>max2 or min2>max1):
        print('NO')
    else:
        print('YES')
        
T = int(input())
for i in range(T):
    ls= list(map(int, input().split()))
    fun(ls)