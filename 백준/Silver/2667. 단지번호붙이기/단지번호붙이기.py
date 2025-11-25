import sys

input = sys.stdin.readline

n = int(input())

graph = [ list(map(int, input().rstrip())) for _ in range(n)]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0  # 방문 처리
        count = 1  # 현재 집 카운트
        # 상하좌우로 이동하면서 연결된 집들을 모두 탐색
        count += dfs(x - 1, y)
        count += dfs(x + 1, y)
        count += dfs(x, y - 1)
        count += dfs(x, y + 1)
        return count
    return 0

# 각 단지의 집 개수를 저장할 리스트
houses = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_count = dfs(i, j)
            houses.append(house_count)

# 총 단지수 출력
print(len(houses))

# 각 단지의 집 수를 오름차순으로 정렬하여 출력
houses.sort()
for count in houses:
    print(count)