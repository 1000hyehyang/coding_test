n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

# 이진 탐색을 위해 시작점과 끝점을 정해주자
start = 0
end = trees[-1]
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total < m: # 만약 총합이 m보다 작다면, 더 많이 잘라야하므로 end를 줄여주자
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
