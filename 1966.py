# https://www.acmicpc.net/problem/1966
import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    level = deque(list(map(int, sys.stdin.readline().split())))  # 중요도
    
    cnt = 1  # 프린트 갯수 카운트
    pt = m  # 궁금한 문서 위치 포인터
    while len(level) > 0:
        if max(level) == level[0]:  # 중요도 제일 높으면 print
            if pt == 0:  # 궁금한 문서 print
                print(cnt)
                break
            else:
                cnt += 1
                pt = (pt - 1) % len(level)  # 포인터 한칸 앞으로
            level.popleft()  # print했으니 제거
        else:
            level.append(level.popleft())  # 중요도 낮으면 맨 뒤로
            if pt == 0:
                pt = len(level) - 1  # 맨 앞에 있었을 경우 포인터를 맨 뒤로
            else:
                pt = (pt - 1) % len(level)
