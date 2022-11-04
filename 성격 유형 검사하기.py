def solution(survey, choices):
    table = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for ans, score in zip(survey, choices):
        if score > 4: #동의
            table[ans[1]] += score - 4
        elif score < 4: #비동의
            table[ans[0]] += 4 - score
            
    result = ""
    if table["R"] >= table["T"]: result += "R"
    else: result += "T"
    if table["C"] >= table["F"]: result += "C"
    else: result += "F"
    if table["J"] >= table["M"]: result += "J"
    else: result += "M"
    if table["A"] >= table["N"]: result += "A"
    else: result += "N"
    
    return result
