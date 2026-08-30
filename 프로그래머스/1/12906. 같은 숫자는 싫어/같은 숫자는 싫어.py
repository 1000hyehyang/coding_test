def solution(arr):
    answer = [arr[0]]
    lst = [0] * len(arr)
    
    for i in range(len(arr)):
        lst[i] = arr[i]
        if i != 0 and arr[i] != lst[i - 1]:
            answer.append(arr[i])

    return answer