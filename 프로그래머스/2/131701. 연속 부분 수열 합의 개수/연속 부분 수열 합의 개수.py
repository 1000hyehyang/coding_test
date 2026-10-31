def solution(elements):
    arr = elements * 2
    result = set()

    for length in range(1, len(elements) + 1):
        for start in range(len(elements)):
            result.add(sum(arr[start:start + length]))

    answer = len(result)
    
    return answer