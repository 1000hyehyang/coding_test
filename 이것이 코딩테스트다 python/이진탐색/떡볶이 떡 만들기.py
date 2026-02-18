n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

# 10 15 17 19

start = 0
end = array[-1]

# 이진 탐색 수행
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        # 잘린 떡 길이 계산
        if x > mid:
            total += x - mid
    # 잘린 떡 양이 부족하면 끝점을 감소시킴       
    if total < m:
        end = mid - 1
    # 잘린 떡 양이 충분하면 시작점을 증가시킴
    else:
        result = mid
        start = mid + 1
        
print(result)