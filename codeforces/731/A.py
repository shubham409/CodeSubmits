import string
def fun(name):
    ls=list(string.ascii_lowercase[:])
    dct={val:i for i ,val in enumerate(ls)}
    count=0
    prv=0
    for i in name:
        val=dct.get(i)
        now=min(abs(val-prv),abs(26-abs(prv-val)))
        count+=now
        prv=val
    print(count)

T=1
for i in range(T):
    name=input()
    fun(name)
