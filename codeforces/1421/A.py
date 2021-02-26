def fun(ls):
    a,b=ls 
    print(a^b)
 
T= int(input())
for i in range(T):
    # n= int(input())
    ls= list(map(int,input().split()))
    fun(ls)