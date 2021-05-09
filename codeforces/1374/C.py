def fun(st):
    ob=0
    cb=0
    for i in st:
        if(i==')'):
            if ob>0:
                ob-=1
            else:
                cb+=1
        else:
            ob+=1
    print((cb+ob)//2)


T = int(input())
for _ in range(T):
    n=int(input())
    st=input()
    fun(st)