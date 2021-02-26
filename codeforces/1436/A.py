def fun(ls,t):
    if(sum(ls)==t):
        print('YES')
    else:
        print('NO')
    

 
T= int(input())
for i in range(T):
    # n= int(input())
    n ,t = list(map(int,input().split()))
    ls= list(map(int,input().split()))
    fun(ls,t)