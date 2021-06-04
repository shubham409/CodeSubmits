from math import gcd

def fun(ls,n):
    even=[]
    rest=[]
    for i in ls:
        if(i%2==0):
            even.append(i)
        else:
            rest.append(i)
    lt= even+rest
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if(gcd(lt[i],2*lt[j])>1):
                count+=1
    print(count)

T = int(input())
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(ls,n)