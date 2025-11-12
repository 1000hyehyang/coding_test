import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))

# 주어진 수들을 M번 더해서 가장 큰 수를 만드는 법칙인데 한 수를 K번 초과해서 더할 수 없다.

numbers.sort()
first = numbers[-1]
second = 0

for i in numbers:
    if i >= second and i < first:
        second = i

result = 0
for i in range(1, m + 1):
    if i % (k + 1) == 0:
        result += second
    else:
        result += first

print(result)