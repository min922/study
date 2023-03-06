# https://www.acmicpc.net/problem/9012
import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    data = list(sys.stdin.readline().strip())
    cnt = 0
    for elt in data:
        if elt == "(":
            cnt += 1
        elif elt == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
