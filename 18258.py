# https://www.acmicpc.net/problem/18258
import sys

n = int(sys.stdin.readline().strip())

queue = []
idx = 0

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(queue) == idx:
            print(-1)
        else:
            print(queue[idx])
            idx += 1
            # print(queue.pop(0)) # 맨 앞요소 pop하고 나머지 한칸씩 당기는 과정에서 O(n)의 연산
    elif cmd[0] == "size":
        print(len(queue) - idx)
    elif cmd[0] == "empty":
        if len(queue) == idx:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(queue) == idx:
            print(-1)
        else:
            print(queue[idx])
    elif cmd[0] == "back":
        if len(queue) == idx:
            print(-1)
        else:
            print(queue[-1])
