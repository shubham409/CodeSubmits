t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    odd=[]; even=[]
    for i in range(n*2):
        if a[i]%2==1:
            odd.append(i+1)
        else:
            even.append(i+1)
    odd=odd[len(odd)%2:]
    even=even[len(even)%2:]
    odd+=even
    for i in range(0, 2*(n-1), 2):
        print(odd[i], odd[i+1])