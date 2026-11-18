N = int(input())
val = 1
cnt = 0

while True:
    if 2 ** cnt == N:
        print(cnt)
        break
    val *= 2
    cnt += 1