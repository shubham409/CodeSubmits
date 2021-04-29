def fun(ls):
    n,m,c=ls
    f=(n-1)*1 + (m-1)*n
    s=(m-1)*1 + (n-1)*m
    # concept :- every path is equal no matter what u choose
    if(f==c):
        print('YES')
    else:
        print('NO')
T = int(input())
for i in range(T):
    ls= list(map(int, input().split()))
    fun(ls)