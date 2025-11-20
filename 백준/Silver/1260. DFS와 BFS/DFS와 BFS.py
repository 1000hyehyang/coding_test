import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

# 인접 리스트 초기화 (노드 번호가 1부터 시작)
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력받아서 인접 리스트에 추가
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

# 각 노드의 인접 리스트를 정렬 (작은 번호부터 방문)
for i in range(1, n + 1):
    graph[i].sort()

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)