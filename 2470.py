# https://www.acmicpc.net/problem/2470
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

left, right = 0, n - 1
ans = abs(data[left] + data[right])
result = []
while left < right:
    tmp = data[left] + data[right]
    if abs(tmp) <= ans:  # 차이가 더 작아지면
        ans = abs(tmp)  # 갱신
        result = [data[left], data[right]]
        if ans == 0:
            break
    if tmp < 0:  # 음수라면 더 크게 만들기
        left += 1
    else:  # 양수라면 더 작게
        right -= 1
print(*result)
