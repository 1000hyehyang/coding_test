# push X: 정수 X를 스택에 넣는 연산이다.
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys

input = sys.stdin.readline
n = int(input())
lst = []

for i in range(n):
    command = input().split()
    order = command[0]
    if len(command) == 2:
        number = int(command[1])
    else:
        number = None
    
    if order == 'push':
        lst.append(number)
    elif order == 'pop':
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(lst))
    elif order == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)
