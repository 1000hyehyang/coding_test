n = int(input())
i = 2
check = True

while i < n:
    if n % i == 0:
        check = False
        break
    i += 1

if check:
    print('P')
else:
    print('C')