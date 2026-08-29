def solution(arr):
    answer = []
    arr_sorted = sorted(arr)
    min_num = arr_sorted[0]
    arr_copy = arr
    for i in arr:
        if i == min_num:
            arr_copy.remove(i)
    
    if len(arr_copy) <= 1:
        return [-1]
    else:
        return arr_copy
    
    return answer