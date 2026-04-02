import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [False] * (v + 1)
heap = [(0, 1)]   # (비용, 정점)
answer = 0
count = 0

while heap and count < v:
    cost, now = heapq.heappop(heap)

    if visited[now]:
        continue

    visited[now] = True
    answer += cost
    count += 1

    for next_cost, next_node in graph[now]:
        if not visited[next_node]:
            heapq.heappush(heap, (next_cost, next_node))

print(answer)