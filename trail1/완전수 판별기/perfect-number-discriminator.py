N = int(input())
total = 0

for i in range(1, N):
    if N % i == 0:
        total += i

if total == N:
    print('P')
else:
    print('N')