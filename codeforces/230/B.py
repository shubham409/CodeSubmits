ls=[True for i in range(10**6+1)]
ls[0] = False
ls[1]=False
st=set()
for i in range(2,len(ls)):
    if(ls[i]==False):
        continue
    for j in range(i+i,len(ls),i):
        ls[j]=False
for i,val in enumerate (ls):
    if(val==True):
        st.add(i*i)
# st =set(i*i for i in st)
# print(st)
t= int(input())
ls= list(map(int,input().split()))
for i in ls :
    if (i in st):
        print('YES')

    else:
        print('NO')