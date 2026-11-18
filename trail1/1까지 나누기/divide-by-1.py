N = int(input())
i = 1
cnt = 0

while N > 1:
    N //= i
    cnt += 1
    if N <= 1:
        print(cnt)
        break
    i += 1