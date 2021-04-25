def fun(a,b,c):
    print(sum(a)-sum(b))
    print(sum(b)-sum(c))


        

T = int(input())
T=1
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    ks= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    ms= list(map(int, input().split()))
    fun(ks,ls,ms)