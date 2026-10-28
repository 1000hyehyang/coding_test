def solution(keymap, targets):
    answer = []
    min_press = {}

    for key in keymap:
        for idx, ch in enumerate(key):
            if idx + 1 < min_press.get(ch, float('inf')):
                min_press[ch] = idx + 1
    
    for target in targets:
        result = 0
        for ch in target:
            if ch in min_press:
                result += min_press.get(ch)
            else:
                result = -1
                break
        answer.append(result)
         
    return answer