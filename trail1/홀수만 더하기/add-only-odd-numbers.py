n = int(input())
total = 0

for i in range(n):
    num = int(input())
    if num % 3 == 0 and num % 2 != 0:
        total += num

print(total)