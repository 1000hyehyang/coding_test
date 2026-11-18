total = 0
cnt = 0

while True:
    n = int(input())

    if n < 20 or n >= 30:
        print(f"{total / cnt :.2f}")
        break
    else:
        total += n
        cnt += 1