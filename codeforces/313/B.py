s=input()
l=[0]
for i in range(len(s)-1):
    l.append(int(s[i]==s[i+1])+l[i])
for i in int(input())*[0]:
    a,b=map(int,input().split())
    print(l[b-1]-l[a-1])