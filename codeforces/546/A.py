def fun(n):
    k,n,w=n
    ans=0
    for i in range(1,w+1):
        ans+=(i*k)
    if ans-n>0:
        print(ans-n)
    else:
        print(0)


    


        

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
# n = int(input())
ls = list(map(int, input().split()))
# n=input()
fun(ls)
