def fun(ls, ly):
    print(max((sum(ls),sum(ly))))
        

# T= int(input())
T=1
for i in range(T):
    ls,ly= input().split()
    ly= list( map(int,list( ly ) ))
    ls= list( map(int,list( ls ) ))
    fun(ls,ly)
