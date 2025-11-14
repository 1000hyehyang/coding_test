import sys

input = sys.stdin.readline

n, m = map(int, input().split())

x, y, direction = map(int, input().split()) # (x, y) 위치에 direction 방향을 바라보고 있음

map_list = []
for _ in range(n):
    map_data = list(map(int, input().split()))
    map_list.append(map_data) # 0은 육지, 1은 바다

directions = [0, 1, 2, 3] # 북 동 남 서

count = 1

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

# 왼쪽으로 회전한다는 것은 direction - 1 하는 것
# 만약 1, 1 에 북쪽 보고 있었으면, 다음에 갈 곳은 현재 위치에서 왼쪽
# 1, 1 에서 왼쪽으로 갈 곳은 1, 0 이다.
# 그러면 1, 0 에 가본 적이 있는지 확인하고, 가본 적이 없으면 그 곳으로 이동한다.
# 가본 적이 있으면 다시 왼쪽으로 회전하고, 가본 적이 없으면 그 곳으로 이동한다.
# 이렇게 하다가 4번 회전했는데 가본 적이 없으면 뒤로 한 칸 이동한다.
# 뒤로 한 칸 이동한 후에도 가본 적이 없으면 원래 있던 곳으로 돌아온다.
# 이렇게 하다가 뒤로 한 칸 이동했는데 가본 적이 있으면 원래 있던 곳으로 돌아온다.
# 이렇게 하다가 뒤로 한 칸 이동했는데 가본 적이 없으면 원래 있던 곳으로 돌아온다.

# 북쪽 보고 있었을 때 왼쪽 이동은 x - 1, y
# 서쪽 보고 있었을 때 왼쪽은 x, y - 1
# 남쪽 보고 있었을 때 왼쪽은 x + 1, y
# 동쪽 보고 있었을 때 왼쪽은 x, y + 1

turn_time = 0
visited = [[False] * m for _ in range(n)]
visited[x][y] = True

while True:
    direction -= 1
    if direction == -1: # 북 -> 서
        direction = 3
    nx = x + dx[direction]
    ny = y + dy[direction]
    if map_list[nx][ny] == 0 and not visited[nx][ny]:
        x = nx
        y = ny
        count += 1
        visited[nx][ny] = True
        turn_time = 0
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break 

print(count)