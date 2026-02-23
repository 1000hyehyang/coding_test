n, k = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

d = [0] * (k + 1)
d[0] = 1

for i in range(n): # 화폐 단위별로 확인
    for j in range(money[i], k + 1):
        d[j] += d[j - money[i]]

print(d[k])