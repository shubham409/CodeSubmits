input()
m=0
for x in map(int,input().split()):
    print(x+m)
    m+=max(0,x)