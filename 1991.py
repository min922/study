# https://www.acmicpc.net/problem/1991
import sys

n = int(sys.stdin.readline().strip())
tree = {}
for _ in range(n):
    a, b, c = sys.stdin.readline().strip().split()
    tree[a] = [b, c]


def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
