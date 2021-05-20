def fun(n):
    ls=[]
    if(n==1):
        print(0)
        return
    for i in range(1,32):
        ls.append(2**i)
    prv=-1
    for i in ls:

        if(i>n):
            break
        prv=i
        
    print((prv-1))
    

T = int(input())
for i in range(T):
    n=int(input())
    fun(n)