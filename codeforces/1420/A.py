for i in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l2=l.copy()
	l.sort(reverse=True)
	if l==l2 and len(set(l))==n:
		print("NO")
	else:
		print("YES")