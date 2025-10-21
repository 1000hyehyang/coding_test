# N의 가장 작은 생성자를 구해내는 프로그램
# 256 -> 245 + 2 + 4 + 5 = 256
import sys

input = sys.stdin.readline
n = int(input())

# x + x의 각 자리 숫자 합 = n
# 반복문 안에서 i + i의 각 자리 숫자 합 = n 이면 i가 생성자
for i in range(1, n):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print(0)
