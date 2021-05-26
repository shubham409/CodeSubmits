def fun(ls,n):
    if(n==1):
        print(1)
        return
    count_non_pos=0
    for i in ls:
        if(i<=0):
            count_non_pos+=1
    ls.sort()
    max_val=10**12
    minimum_pos=max_val
    for i in ls:
        if(i >0):
            minimum_pos= min(minimum_pos,i)
    if(minimum_pos==max_val):
        print(count_non_pos)
        return
    else:
        prv=None
        minimum_alternate_dif=max_val
        for i in ls:
            if(i<=0):
                if(prv==None):
                    prv=i
                else:
                    minimum_alternate_dif=min(minimum_alternate_dif,abs(i-prv))
                    prv=i
        if(minimum_alternate_dif>=minimum_pos):
            print(count_non_pos+1)
        else:
            print(count_non_pos)


    
T = int(input())
for _ in range(T):
    n=list(input())
    ls= list(map(int, input().split()))
    fun(ls,n)