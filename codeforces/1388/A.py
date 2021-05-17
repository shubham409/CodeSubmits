def fun(ls):
    n=ls[0]
    st=[[n-30,6,14,10],[n-39,15,14,10],[n-35,15,14,6],[n-31,15,6,10]]

    if(len(set([n-30,6,14,10]))==4 and n>30):
        print('YES')
        print(n-30,6,14,10)
    else:
        for i in st[1:]:
            if(len(set(i))==4 and n>sum(i[1:])):
                print('YES')
                print(*i)
                return
        print('NO')

T = int(input())
for _ in range(T):
    ls= list(map(int, input().split()))
    fun(ls)