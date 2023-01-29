# https://www.acmicpc.net/problem/1912
import sys

n = int(sys.stdin.readline().strip())

num = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    num[i] = max(num[i], num[i] + num[i - 1])
# 이전 숫자까지 합 중 최댓값을 기록
# i가 1일 경우 만약 num[1]이 더 크다면 num[1]값은 그대로 유지해서 i가 2일경우 num[1]+num[2]의 연속합
# 만약 num[1]+num[0]이 더 크다면 num[1]값에 num[0]+num[1]의 연속합이 됨 그렇게 i가 2가 되면 num[2]와 num[0]+num[1]+num[2]를 비교
# 어차피 최댓값만 구하면 되니까 list를 바로바로 갱신해나감

print(max(num)) # 계산한것 중 최댓값 출력
