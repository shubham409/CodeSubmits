def fun(ls,n):
    st=set(ls)
    dct={i:-1 for i in st}
    for i,j in enumerate(ls):
        if(dct.get(j)==-1):
            dct[j]=i
        else:
            if(i==dct.get(j)+1):
                dct[j]=i
            else:
                print('NO')
                return
    print('YES')

    

T = int(input())
for _ in range(T):
    n=int(input())
    st=input()
    fun(st,n)