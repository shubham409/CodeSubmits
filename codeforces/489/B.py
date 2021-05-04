def fun(n,ln,m,lm):
    ln=sorted(ln)
    lm=sorted(lm)
    len_n=len(ln)
    len_m=len(lm)
    i=0
    j=0
    count=0
    while i<len_n and j < len_m:
        val_n=ln[i]
        val_m=lm[j]
        if(abs(val_m-val_n)<=1):
            count+=1
            i+=1
            j+=1
        else:
            if(val_m<val_n):
                j+=1
            else:
                i+=1
    print(count)

T=1
for _ in range(T):
    n=int(input())
    ln= list(map(int, input().split()))
    m=int(input())
    lm= list(map(int, input().split()))
    fun(n,ln,m,lm)