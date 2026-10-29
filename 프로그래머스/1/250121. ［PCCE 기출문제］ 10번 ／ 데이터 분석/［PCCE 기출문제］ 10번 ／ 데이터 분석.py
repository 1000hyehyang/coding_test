def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    temp = []
    ext_map = ['code', 'date', 'maximum', 'remain']
    
    # ext 값이 val_ext보다 작은 데이터만 뽑는다
    for item in data:
        idx = ext_map.index(ext)
        
        if item[idx] < val_ext:
            temp.append(item)
    
    answer = sorted(temp, key = lambda x : x[ext_map.index(sort_by)])
        
    return answer