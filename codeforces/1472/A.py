def fun(ls):
    w,h,t=ls
    count=1
    while(w%2==0 or h%2==0):
        if(w%2==0):
            w=w//2
            count*=2
        # print(w,h,count)
        if(h%2==0):
            h=h//2
            count*=2
        # print(w,h,count)
        if(count>=t):
            print('yes')
            return
        if(w==0 and h==0):
            break
    if(count>=t):
        print('yes')
        return
    else:
        print('no')


T= int(input())
for i in range(T):
    ls=list(map(int,input().split()))
    # ls= input()
    fun(ls)