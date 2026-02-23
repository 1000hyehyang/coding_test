n, m = map(int, input().split())

듣잡 = set(input() for _ in range(n))
보잡 = set(input() for _ in range(m))

result = sorted(듣잡 & 보잡)

print(len(result))
for name in result:
    print(name)