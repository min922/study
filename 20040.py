# https://www.acmicpc.net/problem/20040
import sys


def find_root(x):
    if tree[x] != x:  # x가 루트노드가 아니라면
        tree[x] = find_root(tree[x])  # 부모의 루트로 바꿔가며 호출
    return tree[x]


def union_set(x, y):
    # 루트노드를 찾아서 루트노드를 같게 바꿔줌
    x = find_root(x)
    y = find_root(y)
    if x <= y:
        tree[y] = x
    else:
        tree[x] = y


n, m = map(int, sys.stdin.readline().split())
tree = [i for i in range(n)]
check = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find_root(a) == find_root(b):  # 사이클 발생시
        print(i + 1)  # 사이클 차례 출력
        check = 1
        break
    union_set(a, b)
if check == 0:  # 사이클 없을때
    print(0)
