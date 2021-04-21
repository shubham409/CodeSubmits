
def fun(ls):
    st=sorted(ls)
    # bn+1 can be 1st last or second last(in case any one before  this is is x) or can be 2nd last if last is x(max value is x)
    temp=st[:-2]
    first_last=st[-1]
    second_last=st[-2]
    sm=sum(temp)
    total=sum(ls)-first_last
    # print(total)
    if(sm==first_last or sm==second_last):
        print(*temp)
        return
    else:
        for i,val in enumerate(st[:-1:]):
            if(total-val==first_last  ):
                print(*(st[:i]+st[i+1:-1]))
                # print(total-val)
                return
    print(-1)



T = int(input())
# T=1
for i in range(T):
    # var=input()
    val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # ls= list(input())
    # qs=list(map(int, input().split()))
    fun(ls)
