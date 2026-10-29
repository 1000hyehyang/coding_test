def solution(X, Y):
    answer = ''
    x_dict = {}
    y_dict = {}
    
    X = ''.join(sorted(X))
    
    Y = ''.join(sorted(Y))
    
    for x in X:
        x_dict[x] = x_dict.get(x, 0) + 1
    
    for y in Y:
        y_dict[y] = y_dict.get(y, 0) + 1
    
    result = {}
    
    for key in x_dict:
        if key in y_dict:
            result[key] = min(x_dict[key], y_dict[key])
    
    print(result)
    
    if len(result) == 0:
        answer = '-1'
    elif len(result) == 1 and '0' in result:
        answer = '0'
    else:
        for item in result:
            answer += item * result.get(item)
        answer = ''.join(sorted(answer, reverse = True))
    
    return answer