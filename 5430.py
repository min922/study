# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

T = int(sys.stdin.readline().strip())

for _ in range(T):
    cmd = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    tmp = sys.stdin.readline().strip()
    data = deque(list(tmp[1:-1].split(",")))
    if n == 0:
        data = deque()
    rev = 0
    is_empty = 0
    for c in cmd:
        if c == "R":
            rev += 1
        elif c == "D":
            if len(data) < 1:
                print("error")
                is_empty = 1
                break
            else:
                if rev % 2 == 0:
                    data.popleft()
                else:
                    data.pop()
    if rev % 2 == 1:
        data.reverse()
    if is_empty == 0:
        print("[" + ",".join(data) + "]")
