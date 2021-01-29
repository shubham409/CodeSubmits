from collections import Counter 

def fun(ls):
    dct= dict(Counter(ls))
    ans=0
    for key, value in dct.items():
        ans=max(value,ans)
    print(ans)
T= int(input())
for i in range(T):
    n= int(input())
    ls=(list(map(int, input().split())))
    fun(ls)
