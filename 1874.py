# https://www.acmicpc.net/problem/1874
import sys

n = int(sys.stdin.readline().strip())
stack = []
num = 1  # 1부터 n까지 돎
result = []  # +, - 입력
is_ok = 0  # result 출력용

for _ in range(n):
    input_num = int(sys.stdin.readline().strip())
    while num <= input_num:
        stack.append(num)
        result.append("+")
        num += 1
    if stack[-1] == input_num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        is_ok = 1
        break

if is_ok == 0:
    for i in result:
        print(i)
