# https://www.acmicpc.net/problem/16139

# 처음에 s 돌면서 다 저장한 후 출력해 O(1)
import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())

dp = [[0] * 26]  # i번째까지 알파벳이 몇번 나왔는지 저장할 배열
dp[0][ord(s[0]) - 97] = 1  # 맨 첫번째 알파벳 1개 저장
for i in range(1, len(s)):  # 두번째부터 돌면서
    dp.append(dp[-1][:])  # i-1번째 센거에다가
    dp[i][ord(s[i]) - 97] += 1  # i번째 알파벳 하나 더해서 저장

for _ in range(q):
    tmp = list(sys.stdin.readline().split())
    l, r = map(int, [tmp[1], tmp[2]])
    if l == 0:  # 맨 처음부터 시작이면
        print(dp[r][ord(tmp[0]) - 97])  # r번째거
    else:
        print(dp[r][ord(tmp[0]) - 97] - dp[l - 1][ord(tmp[0]) - 97])
        # 중간부터면 r - (l-1)하면 l부터 r까지 나옴



# 밑에는 2중 for문으로 시간초과 발생
import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())

for i in range(q):
    t = list(sys.stdin.readline().split())
    a, l, r = t[0], int(t[1]), int(t[2])
    pre_sum = [0 for _ in range(len(s) + 1)]
    for j in range(len(s)):
        if s[j] == a:
            pre_sum[j + 1] = pre_sum[j] + 1
        else:
            pre_sum[j + 1] = pre_sum[j]
    print(pre_sum[r + 1] - pre_sum[l])
