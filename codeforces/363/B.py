def fun(ls,lt):
    n,w=lt
    w=w
    min_val=0
    min_index=0
    sum_sofar=0
    prv=0
    for i,val in enumerate(ls):
        if(i<w):
            sum_sofar+=val
            min_val+=val
        else:
            prv_val=ls[prv]
            temp=sum_sofar+val-prv_val
            prv+=1
            if(temp<min_val):
                min_val=temp
                min_index=prv
            sum_sofar=temp
            
    print(min_index+1)


T = 1
for _ in range(T):
    lt= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,lt)