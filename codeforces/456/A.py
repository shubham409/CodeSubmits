def fun(ls):
    st=sorted(ls)
    # print(st)
    prv=None
    for i in st:
        # print(i)
        if(prv==None):
            prv=i
            continue
        else:
            if(prv[1]>i[1]):
                print('Happy Alex')
                # print(prv[0],i[0])
                return
            prv=i
    print('Poor Alex')

    


    

T = int(input())
ls=[]
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ms= list(map(int, input().split()))
    # n=int(input())
    # ls= list(map(int, input().split()))
    lt= list(map(int, input().split()))
    ls.append([lt[1],lt[0]])
fun(ls)