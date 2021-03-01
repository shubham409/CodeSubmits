def fun(n):
    ls=[1]
    sm=1
    i=1
    while(sm<n):
        
        i+=1
        sm+=i
        ls.append(i)
    if(sm==n):
        print(len(ls))
        print(*ls)
    # else:
    #     ls[-1]=ls[-1]+n-sm
    #     print(*ls)
    if(sm>n):
        v=ls.pop()
        sm=sm-v
        ls[-1]=ls[-1]+n-sm
        print(len(ls))
        print(*ls)
# T= int(input())
# for i in range(T):
t= int(input())
# ls= list(map(int,input().split()))
fun(t)