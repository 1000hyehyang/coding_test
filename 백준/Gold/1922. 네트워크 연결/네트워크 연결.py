import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [False] * (n + 1)
heap = [(0, 1)]   # (비용, 정점)
answer = 0
count = 0

while heap and count < n:
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
