def fun(ls):
    dct = {}
    count = 0
    for i in ls:
        f, s = i
        if(f in dct):
            dct[f] = dct.get(f) + 1
        else:
            dct[f] = 1
        if(s in dct):
            dct[s] = dct.get(s) + 1
        else:
            dct[s] = 1
    for key, value in dct.items():
        if value < 2:
            count += 1
    print(count)


T = int(input())
ls = []
for i in range(T-1):
    lt = list(map(int, input().split()))
    ls.append(lt)
fun(ls)
