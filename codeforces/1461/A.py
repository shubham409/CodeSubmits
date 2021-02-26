def fun(ls):
    n,k=ls 
    s1='cba'
    s2='cb'
    s3='c'
    if((n-k)%3==0):
        print('a'*k+'cba'*((n-k)//3))
    if((n-k)%3==2):
        print('a'*k+'cba'*((n-k)//3)+'cb')
    if((n-k)%3==1):
        print('a'*k+'cba'*((n-k)//3)+'c')
T= int(input())
for i in range(T):
    ls=list(map(int,input().split()))
    fun(ls)