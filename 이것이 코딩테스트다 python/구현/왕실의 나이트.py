import sys

input = sys.stdin.readline

# c2
location = input()

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
}

# location의 좌표를 숫자로 변환하자. 문자는 열 숫자는 행
x = dictionary[location[0]]
y = int(location[1])

# 위 아래로 갔을 때 2칸 이상 있고, 양옆으로 1칸 이상 있는 경우
# 양 옆으로 갔을 때 2칸 이상 있고, 위 아래로 1칸 이상 있는 경우
count = 0

if x - 2 > 0 and y - 1 > 0:
    count += 1
if x - 2 > 0 and y + 1 <= 8:
    count += 1
if x + 2 <= 8 and y - 1 > 0:
    count += 1
if x + 2 <= 8 and y + 1 <= 8:
    count += 1

if y - 2 > 0 and x - 1 > 0:
    count += 1
if y - 2 > 0 and x + 1 <= 8:
    count += 1
if y + 2 <= 8 and x - 1 > 0:
    count += 1
if y + 2 <= 8 and x + 1 <= 8:
    count += 1

print(count)