t=int(input())
for i in range(t):
    ro,be=0,0
    n=int(input())
    s=list(map(int,input()))
    for i in range(n):
        if i%2==0: 
            if s[i]%2==1:ro+=1
        else: 
            if s[i]%2==0:be+=1
    if n%2==1:t= 1 if ro>0 else 2
    else:t= 2 if be>0 else 1
    print(t)