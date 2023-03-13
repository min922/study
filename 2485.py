# https://www.acmicpc.net/problem/2485
import sys, math

n = int(sys.stdin.readline().strip())
tree = []
for _ in range(n):
    tree.append(int(sys.stdin.readline().strip()))
tree.sort()
gcd = tree[1] - tree[0]
for i in range(1, n):
    gcd = math.gcd(gcd, tree[i] - tree[i - 1])  # 나무 사이 간격들의 최대공약수
total = (tree[-1] - tree[0]) // gcd  # 동간격일때의 나무의 갯수
print(total - n + 1)  # 심어야하는 나무의 갯수 - 심어져 있는 갯수 + 맨처음
