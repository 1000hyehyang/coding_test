import sys

input = sys.stdin.readline
n, k = map(int, input().split())

# n을 k로 나누어 떨어지면 나누고, 아니면 1을 빼는 것을 n이 1이 될 때까지 반복
count = 0

while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)