# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline().strip())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
preorder = []
nodeNum = [0 for _ in range(n + 1)]
for i in range(n):
    nodeNum[inorder[i]] = i  # 중위순회 i번째 요소의 index 저장


def find_pre(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return
    root = postorder[postEnd]
    leftRoot = nodeNum[root] - inStart  # root기준으로 앞은 왼쪽서브트리
    rightRoot = inEnd - nodeNum[root]  # 뒤는 오른쪽 서브트리

    print(root, end=' ')
    find_pre(inStart, inStart + leftRoot - 1, postStart, postStart + leftRoot - 1)
    find_pre(inEnd - rightRoot + 1, inEnd, postEnd - rightRoot, postEnd - 1)


find_pre(0, n - 1, 0, n - 1)
