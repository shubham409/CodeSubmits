for _ in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  a=[]
  for i in l:
    if i not in a:
      a.append(i)
  for i in a:
    print(i,end=' ')