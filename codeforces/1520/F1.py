def fun(ls,k):
    n,t=ls
    number_of_zeros=10**12
    number_of_ones=-1
    min_index_with_kzeros=n+1
    l=1
    u=n
    while(l<=u):
        mid=(l+u)//2
        print('?',1,mid)
        number_of_ones=int(input())
        number_of_zeros=mid - number_of_ones
        if(number_of_zeros==k):
            min_index_with_kzeros=min(min_index_with_kzeros,mid)
        if(number_of_zeros<k):
            l=mid+1
        else:
            u=mid-1
    print('!',min_index_with_kzeros)

T=1
for _ in range(T):
    ls= list(map(int, input().split()))
    k=int(input())
    fun(ls,k)