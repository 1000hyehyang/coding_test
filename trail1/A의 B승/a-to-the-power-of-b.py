a, b = map(int, input().split())
total = 1

for i in range(b):
    total *= a

print(total)