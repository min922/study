# https://www.acmicpc.net/problem/9935
import sys

given = sys.stdin.readline().strip()
exp = sys.stdin.readline().strip()

while True:
    if exp not in given:
        if len(given) == 0:
            print("FRULA")
            break
        else:
            print(given)
            break
    else:
        given = list(given)
        stack = []
        for elt in given:
            stack.append(elt)
            tmp = ''.join(stack[-len(exp):])
            if tmp == exp:
                for _ in range(len(exp)):
                    stack.pop()
        given = ''.join(stack).strip()
