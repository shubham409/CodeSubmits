def fun(ls):
    st=''
    lt=sorted(ls)
    for i in lt:
        st+=(str(i)+'+')
    print(st[:-1])
    

# T= int(input())
# for i in range(T):
#     # t= int(input())
ls= list(map(int,input().split('+')))
# st=input()
fun(ls)