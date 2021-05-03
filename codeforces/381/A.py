n=int(input())
a=list(map(int,input().split()))
r=0
s=0
for i in range(n):
	b=max(a[0],a[-1])
	if i%2==0:
		s+=b
	else:
		r+=b	
	a.remove(b)
print(s,r)	