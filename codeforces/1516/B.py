def fun(ls,n):
    if(n==2):
        if(ls[0]==ls[1]):
            print('YES')
        else:
            print('NO')
    else:
        prefix_xor=[]
        for i in ls:
            if(prefix_xor==[]):
                prefix_xor.append(i)
            else:
                prefix_xor.append(i^prefix_xor[-1])
        array_of_two=False
        array_of_three=False
        last_xor=prefix_xor[-1]
        for i in range(n-1):
            if(prefix_xor[i]==last_xor^prefix_xor[i]):
                array_of_two=True
                break
        for i in range(n-2):
            for j in range(i+1,n-1):
                if(prefix_xor[i]==prefix_xor[j]^prefix_xor[i] and prefix_xor[j]^prefix_xor[i]==last_xor^prefix_xor[j]):
                    array_of_three=True
                    break
        if(array_of_two or array_of_three):
            print('YES')
        else:
            print('NO')



T = int(input())
for _ in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(ls,n)