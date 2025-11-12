import sys

input = sys.stdin.readline

n, m = map(int, input().split())

max_value = 0
for i in range(n):
    data = list(map(int, input().split()))
    if min(data) > max_value:
        max_value = min(data)
    else:
        continue

print(max_value)