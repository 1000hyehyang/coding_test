d = [0] * 41

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return d[n]

t = int(input())

# 0이 출력되는 횟수 1이 출력되는 횟수
for _ in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        print(fibonacci(n - 1), fibonacci(n))
