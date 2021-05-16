def fun(ls,n):
    st=sorted(ls)
    if(st==ls):
        print(0)
        return
    else:
        if(st[0]==ls[0] or st[-1]==ls[-1]):
            print(1)
            return
        else:
            if(st[0]==ls[-1] and st[-1]==ls[0]):
                print(3)
                return
            else:
                print(2)
                return

T = int(input())
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))    
    fun(ls,n)