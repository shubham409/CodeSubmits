def fun(st):
    lower,upper=0,0
    for i in st:
        if(i.islower()):
            lower+=1
        else:
            upper+=1
    if(lower>=upper):
        print(st.lower())
    else:
        print(st.upper())
    
        

# T= int(input())
# for i in range(T):
    # ls=list(map(int,input().split()))
st=input()
fun(st)