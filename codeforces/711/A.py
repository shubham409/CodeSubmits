a = '\n'.join(input() for i in range(int(input())))
if 'OO' in a:
    print('YES')
    print(a.replace('OO', '++', 1))
else:
    print('NO')