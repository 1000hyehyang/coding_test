# 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지
# 스택에 push하는 순서는 반드시 오름차순을 지킨다
# push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO

# 4 3 6 8 7 5 2 1
# 이거 만들려면 일단 1 2 3 4 5 6 7 8 이렇게 있는 거에서
# 스택에 1 2 3 4 넣고 4랑 3 뺌 + + + + - -
# 1 2 에다가 5 6 넣고 6 뺌 + + -
# 1 2 5 에다가 7 8 넣고 8 7 5 2 1 뺌 + + - - - - -

import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []
count = 1 # 1부터 n까지의 수를 스택에 넣을 때 사용
possible = True

for i in range(n):
    data = int(input())
    while count <= data: # 스택에 수를 넣을 때까지 반복
        stack.append(count)
        result.append('+')
        count += 1
        
    if stack and stack[-1] == data: # 스택의 맨 위의 수가 입력받은 수와 같으면 빼기
        stack.pop()
        result.append('-')
    else: # 불가능한 경우
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print("NO")