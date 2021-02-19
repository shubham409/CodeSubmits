def fun(ls):
    n=ls[0]
    if(n&(n-1)==0):
        print('no')
        return
    print('yes')
T= int(input())
for i in range(T):
    # t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)