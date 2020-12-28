def part1(left: int, right: int):
    count = 0
    for i in range(left, right + 1):
        if isValid(i):
            count += 1
    return count

def part2(left: int, right: int):
    count = 0
    for i in range(left, right + 1):
        if isValid2(i):
            count += 1
            print(i)
    return count

def isValid(x: int):
    xStr = str(x)
    xLis = list(xStr)
    
    # check if nonincreasing sequence
    for i in range(len(xLis) - 1):
        if int(xLis[i + 1]) < int(xLis[i]):
            return False

    # check repeating digits
    repeat = 0
    for i in range(len(xLis) - 1):
        if int(xLis[i + 1]) == int(xLis[i]):
            repeat += 1
            break
    if repeat == 0:
        return False

    return True

def isValid2(x: int):
    xStr = str(x)
    xLis = list(xStr)
    
    # check if nonincreasing sequence
    for i in range(len(xLis) - 1):
        if int(xLis[i + 1]) < int(xLis[i]):
            return False

    # check repeating digits
    i = 0
    repeat = 0
    while i < len(xLis):
        tmp = int(xLis[i])
        numSame = 0
        while int(xLis[i]) == tmp:
            i += 1
            numSame += 1
            if i == len(xLis):
                break
        if numSame == 2:
            repeat = 1
            break
        
    if repeat != 1:
        return False
    
    return True
