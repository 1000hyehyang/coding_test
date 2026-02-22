n, k = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

d = [100001] * (k + 1)
d[0] = 0

for i in range(n): # 화폐 단위별로 확인
    for j in range(money[i], k + 1):
        if d[j - money[i]] != 100001:
            d[j] = min(d[j], d[j - money[i]] + 1)

if d[k] == 100001:
    print(-1)
else:
    print(d[k])