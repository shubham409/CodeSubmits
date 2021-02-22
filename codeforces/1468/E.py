def fun(ls):
    ls=sorted(ls)
    print(ls[0]*ls[2])
    
 
T= int(input())
for i in range(T):
    # t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)