def fun(n=int(input())):
    val= 0
    for i in range (n):
        ipt = input()
        if ipt == '++X' or ipt =='X++':
            val+=1
        else:
            val-=1
    print(val)
fun()