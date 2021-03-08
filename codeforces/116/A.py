def fun(ls):
    prv_enter=0
    prv_exit=0
    ans=0
    p=0
    for exit,enter in ls:
        p=p+enter-exit
        ans=max(ans,p)
    print(ans)






T=int(input())
ls=[]
for i in range(T):
    lt= list(map(int,input().split()))
    ls.append(lt)
fun(ls)