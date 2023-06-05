# https://www.acmicpc.net/problem/5639
import sys

sys.setrecursionlimit(10 ** 9)

preorder = []
n = 0
while True:
    try:
        preorder.append(int(sys.stdin.readline().strip()))
        n += 1
    except:
        break


def find_post(preStart, preEnd):
    if preStart > preEnd:
        return
    mid = preEnd + 1
    root = preorder[preStart]
    for i in range(preStart + 1, preEnd + 1):
        if preorder[i] > root:
            mid = i
            break
    find_post(preStart + 1, mid - 1)
    find_post(mid, preEnd)
    print(root)


find_post(0, n - 1)
