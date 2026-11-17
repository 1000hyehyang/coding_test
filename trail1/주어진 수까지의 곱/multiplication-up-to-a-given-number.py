a, b = map(int, input().split())
total = 1

for i in range(a, b + 1):
    total *= i

print(total)