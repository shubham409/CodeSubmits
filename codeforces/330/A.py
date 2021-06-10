r, c = map(int, input().split())
a = set()
b = set()
for i in range(r):
	d = input()
	for j in range(len(d)):
		if d[j] == 'S':
			a.add(j)
			b.add(i)
print(r*c-len(a)*len(b))