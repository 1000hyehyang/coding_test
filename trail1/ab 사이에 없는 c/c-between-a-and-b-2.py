a, b, c = map(int, input().split())
check = True # c의 배수가 없다

for i in range(a, b + 1):
    if i % c == 0:
        check = False # c의 배수가 있다

if check:
    print('YES')
else:
    print('NO')