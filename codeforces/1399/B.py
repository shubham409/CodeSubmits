f=int(input())
for q in range(f):
  n=int(input())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  c=0
  for i in range(n):
    c+=max(a[i]-min(a),b[i]-min(b))
  print(c)