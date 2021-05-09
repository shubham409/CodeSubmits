def fun(ls):
    m=max(ls)
    count=0
    for i in range(m,7):
        count+=1
    total=6
    for i in range(1,7):
        if(count%i==0 and total%i==0):
            count=count//i
            total=total//i
    print(f'{count}/{total}')

T=1
for _ in range(T):

    ls= list(map(int, input().split()))
    fun(ls)
