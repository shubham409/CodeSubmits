T=int(input())
for _ in range(0,T):
	n,a,b,c,d=map(int,input().split())
	if c+d<(a-b)*n or (a+b)*n<c-d:
		print("No")
	else:
		print("Yes")