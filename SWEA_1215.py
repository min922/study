# SWEA 1215. [S/W 문제해결 기본] 3일차 - 회문1
import sys

for num in range(1, 10):
    n = int(sys.stdin.readline().strip())
    board = [list(sys.stdin.readline().strip()) for _ in range(8)]
    result = 0
    
    for j in range(8):
        for i in range(8 - n + 1):
            row = board[j][i:i + n]
            if row == row[::-1]:
                result += 1
    
    rev_board = []
    for i in range(8):
        tmp = [elt[i] for elt in board]
        rev_board.append(tmp)
    for j in range(8):
        for i in range(8 - n + 1):
            row = rev_board[j][i:i + n]
            if row == row[::-1]:
                result += 1
    print('#{} {}'.format(num, result))
