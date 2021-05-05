def fun(n):
    if(n>=1 and n<=9):
        print(n)
    else:
        l=len(str(n))
        sure=(l-1)*9
        for i in range(1,10):
            now=f'{i}'
            now=int(now*l)
            if(n>=now):
                sure+=1
            else:
                break
        print(sure)


T = int(input())
for _ in range(T):
    n=int(input())
    fun(n)