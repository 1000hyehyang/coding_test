# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

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
            print(lst.pop(0))
        else:
            print(-1)
    elif order == 'size':
        print(len(lst))
    elif order == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif order == 'back':
        if lst:
            print(lst[-1])
        else:
            print(-1)
