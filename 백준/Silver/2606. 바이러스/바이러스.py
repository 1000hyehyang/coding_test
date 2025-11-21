import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
m = int(input())

# 인접 리스트 초기화 (노드 번호가 1부터 시작)
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력받아서 인접 리스트에 추가
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True) - 1)