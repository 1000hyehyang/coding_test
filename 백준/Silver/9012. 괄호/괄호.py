import sys

input = sys.stdin.readline
n = int(input())

pair = {')' : '('}

for i in range(n):
    str = input()
    stack = []
    for j in str:
        if j in pair.values():
            stack.append(j)
        elif j in pair.keys():
            if not stack or stack[-1] != pair[j]: # 닫는 괄호가 나왔는데 스택이 비어있거나 스택의 맨 위가 짝이 아니면 실패
                stack.append(j) 
                break 
            else:
                stack.pop()
    if stack:
        print("NO")
    else:
        print("YES")