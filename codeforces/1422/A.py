def fun(ls):
    # A quadrilateral can be built when max(a,b,c,d)<a+b+c+d−max(a,b,c,d), that is, the sum of the minimum three numbers is greater than the maximum. To do this, you could choose max(a,b,c) or a+b+c−1 as d
    
    print(sum(ls)-1)
T= int(input())
for i in range(T):
    # t= int(input())
    ls= list(map(int,input().split()))
    # st= input()
    # t= input()
    # fun(st)
    fun(ls)