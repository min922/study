# https://www.acmicpc.net/problem/17298
import sys

n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and (stack[-1][0] < num[i]):  # 스택이 비어있지 않고 스택 맨 위가 num[i]보다 작을때까지
        tmp, idx = stack.pop()
        result[idx] = num[i]  # idx에 num[i] 추가
    stack.append([num[i], i])  # 스택이 비어있으면 현재 값 추가
print(*result)
