def get(first_prime_above):
    for i in range(first_prime_above, 10**12):
        j=2
        found_prime=True
        while j*j<=i:
            if(i%j==0):
                found_prime=False
                break
            j+=1
        if(found_prime):
            return i

from math import floor,ceil    
def fun(st):
    d = st
    first_prime = get(1 + d)

    second_prime = get(d+first_prime)
    print(first_prime * second_prime)
    


T= int(input())
for i in range(T):
    # t= int(input())
    # ls= list(map(int,input().split()))
    st= input()
    fun(int(st))