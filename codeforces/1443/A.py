def fun(n):
   ls=[i for i in range(2*n,4*n,2)]
   print(*ls)
        
T = int(input())
for i in range(T):
    t= int(input())
    fun(t)