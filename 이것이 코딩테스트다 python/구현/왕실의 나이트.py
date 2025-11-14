import sys

input = sys.stdin.readline

# c2
location = input().rstrip()

# location의 좌표를 숫자로 변환하자. 문자는 열 숫자는 행
x = int(ord(location[0])) - int(ord('a')) + 1
y = int(location[1])

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
count = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)