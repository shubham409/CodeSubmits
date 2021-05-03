from math import ceil,sqrt,floor

def fun(n):
    if(n%2!=0 and n%4!=0):
        print('NO')
        return
    if(n%2==0):
        s=sqrt(n//2)

        if(ceil(s)==floor(s)):
            print('YES')
            return
    if(n%4==0):
        s=sqrt(n//4)

        if(ceil(s)==floor(s)):
            print('YES')
            return
    print('NO')      


T = int(input())
for i in range(T):
    n=int(input())
    fun(n)





