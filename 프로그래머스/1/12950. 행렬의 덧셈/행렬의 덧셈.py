def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        lst = []
        for j in range(len(arr1[0])):
            a = arr1[i][j] + arr2[i][j]
            lst.append(a)
        answer.append(lst)
        
    return answer