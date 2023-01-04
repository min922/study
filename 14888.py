# https://www.acmicpc.net/problem/14888
import sys, itertools

N = int(sys.stdin.readline().strip())

numbers = list(map(int, sys.stdin.readline().strip().split()))
op = list(map(int, sys.stdin.readline().strip().split()))
add, sub, mul, div = op[0], op[1], op[2], op[3]

maxi = -10e9
mini = 10e9

# 재귀를 이용한 dfs 사용 -> 시간 훨씬 단축됨
def dfs(depth, arr, add, sub, mul, div):
    global maxi, mini
    if depth == N:
        maxi = max(maxi, arr)
        mini = min(mini, arr)
    else:
        if add > 0:
            add -= 1
            dfs(depth + 1, arr + numbers[depth], add, sub, mul, div)
            add += 1
        if sub > 0:
            sub -=1
            dfs(depth + 1, arr - numbers[depth], add, sub, mul, div)
            sub += 1
        if mul > 0:
            mul -=1
            dfs(depth + 1, arr * numbers[depth], add, sub, mul, div)
            mul += 1
        if div > 0:
            div -=1
            dfs(depth + 1, int(arr / numbers[depth]), add, sub, mul, div)
            div += 1
dfs(1, numbers[0], add, sub, mul, div)
print(maxi)
print(mini)

# 전체 가능한 모든 경우의 수 계산
# Python3에서는 시간 초과, PyPy에서는 통과
tmp_op = []
tmp_op.extend(["+"]*op[0])
tmp_op.extend(["-"]*op[1])
tmp_op.extend(["*"]*op[2])
tmp_op.extend(["/"]*op[3])
operators = list(itertools.permutations(tmp_op))
op_num = sum(op)

maxi = -10e9
mini = 10e9
for oper in operators:
    tmp = numbers.copy()
    oper = list(oper)
    total = tmp.pop(0)
    while len(tmp) != 0:
        op = oper.pop(0)
        if op == "+":
            total += tmp.pop(0)
        elif op == "-":
            total -= tmp.pop(0)
        elif op == "*":
            total *= tmp.pop(0)
        elif op == "/":
            total = int(total / tmp.pop(0))
    if total > maxi:
        maxi = total
    if total < mini:
        mini = total

print(maxi)
print(mini)
