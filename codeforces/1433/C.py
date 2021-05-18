for _ in range(int(input())):
	n = int(input())
	s = list(map(int,input().split()))
	m = max(s)
	ind=-1
	for i in range(len(s)):
		if s[i] == m and ((i>0 and s[i] > s[i-1]) or (i < n-1 and s[i] > s[i+1])):
			ind=i+1
	print(ind)
		
