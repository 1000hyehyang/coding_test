k, n = map(int, input().split())

cables = [int(input()) for _ in range(k)]
cables.sort()

# 457 539 743 802

start = 1
end = cables[-1]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for cable in cables:
        if cable >= mid:
            count += cable // mid
    # 만약 count가 n보다 크거나 같으면 더 긴 길이로 잘라야 함
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)