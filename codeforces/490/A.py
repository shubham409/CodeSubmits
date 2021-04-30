input()
a = [int(x) for x in input().split()]
k = min(a.count(1), a.count(2), a.count(3))
print(k)
for i in range(k):
    print(a.index(1) + 1, a.index(2) + 1, a.index(3) + 1)
    a[a.index(1)] = 0
    a[a.index(2)] = 0
    a[a.index(3)] = 0