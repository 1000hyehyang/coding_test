N = int(input())
total = 0

for i in range(N):
    num = int(input())
    total += num

avg = total / N

print(total, f"{avg:.1f}")