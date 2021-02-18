from math import floor
import sys

def fun(ls):
    a=ls[0]
    b=ls[1]
    count_operations=0
    ans=1000
    if(b<=30):
        if(b == 1):
            b += 1
            count_operations += 1
        second_operation = 0 
        while(b <= 30):
            first_operation = 0
            temp_a=a
            temp_b=b
            while temp_a>0:
                temp_a=floor(temp_a/temp_b)
                first_operation+=1
            ans=min(ans, first_operation+second_operation+count_operations)
            b+=1
            second_operation+=1
            
        
    else:
        first_operation = 0
        temp_a=a
        temp_b=b
        while temp_a>0:
            temp_a=floor(temp_a/temp_b)
            first_operation+=1
        ans=min(ans, first_operation+count_operations)
    print(ans)

T= int(input())
for i in range(T):
    # t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)