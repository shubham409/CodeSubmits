for _ in range(int(input())):
   n,k=map(int,input().split(" "))
   l=list(map(int,input().split(" ")))
   l.sort()
   su=sum(l)
   a=n
   for i in l:
      if su//a>=k:
         break
      a=a-1
      su-=i
   print(a)
      