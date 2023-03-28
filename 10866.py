# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque()
for _ in range(n):
    cmdlist = sys.stdin.readline().split()
    cmd = cmdlist[0]
    if cmd == "push_front":
        queue.appendleft(int(cmdlist[1]))
    elif cmd == "push_back":
        queue.append(int(cmdlist[1]))
    elif cmd == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
