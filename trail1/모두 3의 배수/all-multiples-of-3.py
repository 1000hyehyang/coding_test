check = True

for i in range(5):
    n = int(input())
    if n % 3 != 0:
        check = False
        break

if check:
    print(1)
else:
    print(0)