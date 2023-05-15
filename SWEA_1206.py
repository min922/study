# SWEA 1206. [S/W 문제해결 기본] 1일차 - View
import sys

for j in range(10):
    n = int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(2, n - 2):
        cut = data[i - 2:i + 3]  # i를 중심으로 양쪽 거리 2 탐색
        tmp = list(sorted(cut))
        if tmp[-1] == cut[2]:  # 현재 빌딩이 가장 높으면
            result += cut[2] - tmp[-2]  # 조망권 확보된 층 추가
    print("#{} {}".format(j + 1, result))
