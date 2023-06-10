# https://www.acmicpc.net/problem/4195
import sys

sys.setrecursionlimit(10 ** 9)


def find_root(x):
    if tree[x] != x:  # x가 루트노드가 아니라면
        tree[x] = find_root(tree[x])  # 부모의 루트로 바꿔가며 호출
    return tree[x]


def union_friend(x, y):
    # 루트노드를 찾아서 루트노드를 같게 바꿔줌
    x = find_root(x)
    y = find_root(y)
    if x == y:
        return
    else:
        tree[y] = x  # 루트노드 같게 바꿔주고
        visited[x] += visited[y]  # 탐색 횟수 더해줌


t = int(sys.stdin.readline().strip())
for _ in range(t):
    f = int(sys.stdin.readline().strip())
    tree = {}
    visited = {}
    for _ in range(f):
        a, b = sys.stdin.readline().split()
        if a not in tree:
            tree[a] = a
            visited[a] = 1
        if b not in tree:
            tree[b] = b
            visited[b] = 1
        union_friend(a, b)
        print(visited[find_root(a)])
