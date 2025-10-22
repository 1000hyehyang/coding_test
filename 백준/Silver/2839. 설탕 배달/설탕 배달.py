# 3x + 5y = n 인 x, y 쌍 중 x + y가 최소인 것을 구하시오.
# 단, x, y쌍이 없으면 -1 출력.


import sys

input = sys.stdin.readline

n = int(input())

for x in range(n // 3 + 1):
    remainder = n - 3 * x
    if remainder % 5 == 0:
        y = remainder // 5
        print(x + y)
        break
else:
    print(-1)