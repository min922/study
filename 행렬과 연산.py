def ShiftRow(rc):
    rc.insert(0, rc.pop())
    return rc

def Rotate(rc):
    Rotatelist = []

    row = len(rc)
    col = len(rc[0])

    rc1 = rc[0]
    rc2 = [i[-1] for i in rc]
    rc3 = list(reversed(rc[-1]))
    rc4 = list(reversed([i[0] for i in rc])) #테두리 리스트

    Rotatelist = rc1 + rc2[1:] + rc3[1:] + rc4[1:-1] #테두리를 원형으로 이어붙힘
    Rotatelist.insert(0, Rotatelist.pop())

    rc1 = Rotatelist[:col]
    rc2 = Rotatelist[col-1:(col-1)+row]
    rc3 = list(reversed(Rotatelist[(col-1)+row-1 : (col-1)+row-1+col]))
    rc4 = list(reversed(Rotatelist[(col-1)+row-1+col-1:] + Rotatelist[0:1])) #한칸씩 돌린 list

    result = []
    for i in range(len(rc)):
        if i == 0:
            result.append(rc1)
        elif i == (len(rc)-1):
            result.append(rc3)
        else:
            tmp = []
            tmp.append(rc4[i])
            for j in rc[i][1:-1]:
                tmp.append(j)
            tmp.append(rc2[i])
            result.append(tmp)
    return result


def solution(rc, operations):
    for op in operations:
        if op == "ShiftRow":
            rc = ShiftRow(rc)
        elif op == "Rotate":
            rc = Rotate(rc)
    return rc
