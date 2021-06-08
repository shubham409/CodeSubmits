for _ in range(int(input())):
   n, m = map(int, input().split())
   t = 0
   for _ in range(n):
      a, b = map(int, input().split())
      c, d = map(int, input().split())
      if b==c: t+=1
   if t==0 or m%2==1: print('NO')
   else: print('YES')
