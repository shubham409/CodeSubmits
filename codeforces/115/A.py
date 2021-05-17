n = int(input())
p=[int(input()) for i in range(n)]
g=0
for i in range(n):
	c=0
	while i>=0:
		i=p[i]-1
		c+=1
	g=max(g,c)
print(g)
	