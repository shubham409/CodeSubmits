from collections import Counter
def fun(ls):
    dct=Counter(ls)
    mx=max(dct.values())
    for i,j in dct.items():
        if(j==mx):
            print(i)
            return
T = int(input())
ls=[]
for i in range(T):
    st=input()
    ls.append(st)
fun(ls)
