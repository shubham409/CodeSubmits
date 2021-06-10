for i in range(int(input())):
    x = int(input())
    n = list(map(int, input().split()))
    c = n.count(0)
    print(c + (sum(n) + c == 0))