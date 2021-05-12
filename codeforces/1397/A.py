from collections import Counter
def fun(st,val): 
    ct=Counter(st)
    for i,j in ct.items():
        if(j%val!=0):
            print('NO')
            return
    print('YES')

T = int(input())
for i in range(T):
    val=int(input())
    st=''
    for i in range(val):
        st+=input()
    fun(st,val)
    