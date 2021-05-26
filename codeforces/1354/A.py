for _ in range(int(input())):
	a, b, c, d = map(int, input().split())
	if a<=b:
		print(b)
	elif c<=d:
		print(-1)
	else:
		print(((a-b+c-d-1)//(c-d))*c+b)
