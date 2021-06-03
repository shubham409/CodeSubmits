for _ in range(int(input())):
    n = int(input())
    s = set(map(int, input().split()))
    print([1, 2][any(e - 1 in s for e in s)])