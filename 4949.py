# https://www.acmicpc.net/problem/4949
import sys

while True:
    data = list(sys.stdin.readline().rstrip())
    if data == ["."]:
        break
    else:
        stack = []
        for elt in data:
            if elt == "(" or elt == "[":
                stack.append(elt)
            elif elt == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(elt)
            elif elt == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(elt)
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
