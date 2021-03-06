def fun(ls,lt):
    a,b=ls
    c,d=lt
    if(max(a,b)==max(c,d) and min(a,b)+min(c,d)==max(a,b)):
        print('Yes')
    else:
        print('No')


    


        

T = int(input())
for i in range(T):
    # n = list(map(int, input().split()))
    # n = int(input())
    ls = list(map(int, input().split()))
    lt = list(map(int, input().split()))
    # n=input()
    fun(ls,lt)