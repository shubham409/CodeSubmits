from math import floor,gcd

from collections import Counter

def fun(s,t):
    if(len(s)>=len(t)):
        s,t=t,s
        sl=len(s)
        tl=len(t)
    else:
        s,t=t,s
        sl=len(s)
        tl=len(t)
    q=sl//tl    

    lcm = sl*tl//gcd(sl,tl)
    qs=lcm//sl
    qt=lcm//tl
    if (q*t==s):
        print(s)

    elif (s*qs==t*qt):
        print(s*qs)
    else:
        print(-1)
    


    


T= int(input())
for i in range(T):
    # t= int(input())
    # n= int(input())
    # m= int(input())
    # n,u,v= list(map(int,input().split()))
    # ls= list(map(int,input().split()))
    # fun(ls,u,v)
    s=input()
    t=input()
    # fun(s,t,n,m)
    # st= int(input())
    # st= (input())
    fun(s,t)