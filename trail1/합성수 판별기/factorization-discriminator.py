n = int(input())
i = 2
check = False

while i < n:
    if n % i == 0:
        check = True
        break
    i += 1

if check:
    print('C')
else:
    print('N')