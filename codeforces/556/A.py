def fun(st,n):        
    one=0
    zero=0
    for i in st:

        if i=='0':
            zero+=1
        else:
            one+=1
    print(abs(one-zero))

T=1
for i in range(T):
    n=input()
    st=input()
    fun(st,n)