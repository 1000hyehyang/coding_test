import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로길이 M과 세로길이 N
    graph = [ [0] * m for _ in range(n)]    # 배추밭

    baechu = [ list(map(int, input().split())) for _ in range(k)]

    for i in range(k):
        graph[baechu[i][1]][baechu[i][0]] = 1

    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)