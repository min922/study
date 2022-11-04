def solution(board, moves):
    answer = 0
    box = []

    moves = [i-1 for i in moves]
    for move in moves:
        tmp = [row[move] for row in board]
        for idx, t in enumerate(tmp):
            if t != 0:
                if (len(box) != 0) and (box[-1] == tmp[idx]):
                    answer += 2
                    del box[-1]
                else: box.append(tmp[idx])
                board[idx][move] = 0
                break

    return answer
