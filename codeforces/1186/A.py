def fun(ls):
    a,b,c=ls
    if(a<=b and a<=c):
        print('YES')
    else:
        print('NO')

T=1
for i in range(T):
    ls= list(map(int, input().split()))
    fun(ls)
