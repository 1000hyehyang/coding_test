t = int(input())

def solution(n, coins, m):
    d = [0] * (m + 1)
    d[0] = 1
    for coin in coins:
        for j in range(coin, m + 1):
            d[j] += d[j - coin]
    return d[m]

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input()) # 만들어야 하는 금액
    print(solution(n, coins, m))