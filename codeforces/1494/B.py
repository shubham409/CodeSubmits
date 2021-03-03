def fun(n,u,r,d,l):
    ls=[u,r,d,l]
    if(u==n and d==n):
        if(l<2 or r<2):
            print('no')
            return
    if((u==n-1 and d== n) or (d==n-1 and u==n)):
        if((l>=1 and r>=2) or  (l>=2 and r>=1)):
            pass
        else:
            print('no')
            return
    if(l==n and r==n):
        if(u<2 or d<2):
            print('no')
            return
    if((l==n-1 and r== n) or (r==n-1 and l==n)):
        if((u>=1 and d>=2) or  (u>=2 and d>=1)):
            pass
        else:
            print('no')
            return



    if((u==n and d<n-1) or (d==n and u<n-1)):
        if(l<1 or r<1):
            print('no')
            return

    if((l==n and r<n-1) or (r==n and l<n-1)):
        if(u<1 or d<1):
            print('no')
            return




    if((u==n-1 and d<n-1) or (d==n-1 and u<n-1)):
        if((l>=1 and r>=0) or (r>=1 and l>=0)):
            pass
        else:
            print('no')
            return
    if((l==n-1 and r<n-1) or (r==n-1 and l<n-1)):
        if((u>=1 and d>=0) or (d>=1 and u>=0)):
            pass
        else:
            print('no')
            return
    if(l==n-1 and r==n-1):
        if((u>=2 and d>=0) or (d>=2 and u>=0) or (d>=1 and u>=1)):
            pass
        else:
            print('no')
            return
    if(u==n-1 and d==n-1):
        if((l>=2 and r>=0) or (r>=2 and l>=0) or (l>=1 and r>=1)):
            pass
        else:
            print('no')
            return        
    print('yes')
T= int(input())
for i in range(T):
    # t= int(input())
    n,u,r,d,l= list(map(int,input().split()))
    fun(n,u,r,d,l)