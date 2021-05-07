def fun(ls):
    a,b=ls
    if(b==1):
        print('NO')
    elif b==2:
        print('YES')
        print(1*a,3*a,4*a)
    else:
        print('YES')
        print(1*a,(b-1)*a,a*b)        


T = int(input())
for _ in range(T):
    ls= list(map(int, input().split()))
    fun(ls)