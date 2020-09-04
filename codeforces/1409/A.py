from math import ceil
def fun(a,b):
    i=max(a,b)
    j=min(a,b)
    c= i-j
    print(ceil(c/10))


T = int(input())
for i in range(T):
    a,b= input().split()
    fun(int(a),int(b))
