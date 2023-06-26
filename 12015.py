# https://www.acmicpc.net/problem/12015
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
data = [0] + data
dp = [0]

for i in data:
    if dp[-1] < i: # dp의 맨 마지막보다 i가 더 크면(증가하면)
        dp.append(i) # dp에 추가
    else:
        left, right = 0, len(dp) # dp를 이분탐색
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < i:
                left = mid + 1
            else:
                right = mid
        # dp에서 i가 들어갈 수 있는 자리 찾아서 i로 바꿔줌(추가 x)
        dp[right] = i
print(len(dp) - 1)
