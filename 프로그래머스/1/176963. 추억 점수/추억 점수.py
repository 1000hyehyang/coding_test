def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for ph in photo:
        result = 0
        
        for i in ph:
            print(i)
            result += dic.get(i, 0)

        answer.append(result)
        
    return answer