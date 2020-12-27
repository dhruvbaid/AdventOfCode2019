def part1():
    with open("Day 1 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n; character
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())
    
    res = 0
    for i in range(len(lines)):
        res += int(lines[i]/3) - 2

    return res

def part2():
    with open("Day 1 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n; character
    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())
    
    res = 0
    for i in range(len(lines)):
        curAmount = lines[i]
        while curAmount > 0:
            curAmount = int(curAmount/3) - 2
            if curAmount > 0:
                res += curAmount

    return res
