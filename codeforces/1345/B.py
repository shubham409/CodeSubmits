for i in range(int(input())):
	n = int(input())
	count = 0
	while n > 1:
		d = ((24*n+1)**0.5  - 1)//6
		n -= d*(3*d+1)//2
		count += 1
	print(count)
		
