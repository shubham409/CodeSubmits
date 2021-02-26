def fun(ls):
    x,y,z=ls 
    if(x==y and x>z):
        print('yes')
        print(x,z,z)
        return
    if(x==z and x>y):
        print('yes')
        print(x,y,y)
        return
    if(y==z and y>x):
        print('yes')
        print(y,x,x)
        return
    if(x==y==z):
        print('yes')
        print(x,x,x)
        return
    print('no')

 
T= int(input())
for i in range(T):
    # n= int(input())
    ls= list(map(int,input().split()))
    fun(ls)
    