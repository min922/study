# https://www.acmicpc.net/problem/9252
import sys

fir = [""] + list(sys.stdin.readline().strip())
sec = [""] + list(sys.stdin.readline().strip())
result = [[""] * len(sec) for _ in range(len(fir))]
# result[i][j] : fir의 i번째, sec의 j번째의 LCS

for i in range(1, len(fir)):
    for j in range(1, len(sec)):
        if fir[i] == sec[j]:
            result[i][j] = result[i - 1][j - 1] + fir[i]
            # 공통이면 그 전까지 LCS에다가 이번꺼 더하기
        else:
            # 다르면 LCS 중 최댓값 저장
            if len(result[i - 1][j]) >= len(result[i][j - 1]):
                result[i][j] = result[i - 1][j]
            else:
                result[i][j] = result[i][j - 1]

ans = result[-1][-1]
print(len(ans))
print(ans)
