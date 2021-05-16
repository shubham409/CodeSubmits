from math import gcd
def fun(ls):
    k=ls[0]
    f=k
    s=100-k
    val=gcd(f,s)
    while(val!=1):
        f=f//val
        s=s//val
        val=gcd(f,s)
    print(f+s)

T = int(input())
for i in range(T):
    ls= list(map(int, input().split()))    
    fun(ls)