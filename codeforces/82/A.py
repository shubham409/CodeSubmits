def fun(n):
    power_of_two=0
    sm=5
    prv_sum=0
    while(sm<n):
        power_of_two+=1
        prv_sum=sm
        sm+=5*(2**power_of_two)
    each_block=(2**power_of_two)
    ls=["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    for i in range(0,5):
        j=i+1
        if(prv_sum+(each_block*j)>=n):
            print(ls[i])
            return



    

# T = int(input())
T=1
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ms= list(map(int, input().split()))
    n=int(input())
    # ls= list(map(int, input().split()))
    fun(n)