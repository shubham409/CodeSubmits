def fun(ls):
    print(len(set(ls)))


                             

T = int(input())
for _ in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(ls)