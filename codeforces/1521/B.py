from math import gcd
from itertools import cycle
def fun(ls):
    prv=None
    primes=[1000000007,1000000409]
    count=0
    ans=[]
    c=cycle(primes)
    for i in range(n):
        now=ls[i]
        if(i==0):
            prv=now
        else:
            if(gcd(now,prv)!=1):
                if(now<=prv):
                    # now is lesser
                    get_prime=next(c)
                    ans.append([i-1+1 , i+1 , get_prime,min(prv,now)])
                    ls[i]=min(prv,now)
                    count+=1
                    prv=min(prv,now)
                else:
                    # prv is lesser
                    get_prime=next(c)
                    ans.append([i-1+1 , i+1 ,min(prv,now),get_prime])
                    ls[i]=get_prime
                    count+=1
                    prv=get_prime
            else:
                prv=now
            
    if(count==0):
        print(count)
    else:
        print(count)
        for i in ans:
            print(*i)


T = int(input())
for _ in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(ls)