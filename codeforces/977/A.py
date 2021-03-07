def fun(ls):
    n,k=ls
    count=0
    for i in range(k):
        if(n%10==0):
            n//=10
        else:
            n-=1
    print(n)       


    
        

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
# n = int(input())
ls = list(map(int, input().split()))
fun(ls)
