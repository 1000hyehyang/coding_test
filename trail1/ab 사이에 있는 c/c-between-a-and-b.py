a, b, c = map(int, input().split())
check = False

for i in range(a, b + 1):
    if i % c == 0:
        check = True
        break

if check:
    print('YES')
else:
    print('NO')