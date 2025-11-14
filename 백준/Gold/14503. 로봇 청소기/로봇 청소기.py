import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]

robot_map = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
visited[r][c] = True
count = 1
turn_time = 0

def turn_left():
    global d
    d -= 1 # 왼쪽으로 회전
    if d == -1:
        d = 3
    return d

while True:
    turn_left()
    nx = r + dx[d]
    ny = c + dy[d]
    if robot_map[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        r = nx
        c = ny
        count += 1
        turn_time = 0
    else:
        turn_time += 1
    if turn_time == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if robot_map[nx][ny] == 0:
            r = nx
            c = ny
            turn_time = 0
        else:
            break

print(count)