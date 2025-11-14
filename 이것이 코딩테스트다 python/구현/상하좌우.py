import sys

input = sys.stdin.readline
n = int(input())

data = input().split()

x, y = 1, 1

for dir in data:
    if dir == 'L' and x > 1:
        x -= 1
    elif dir == 'R' and x < n:
        x += 1
    elif dir == 'U' and y > 1:
        y -= 1
    elif dir == 'D' and y < n:
        y += 1

print(y, x)