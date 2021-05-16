j=int(input())
for i in range(j):
	n,m=map(int,input().split())
	if n*m<=(n+m):print("YES")
	else:print("NO")