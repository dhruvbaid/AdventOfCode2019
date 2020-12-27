# main :  
def main():
    with open("Day 3 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    # remove '\n' character and split each instruction
    for i in range(len(lines)):
        lines[i] = lines[i].split(",")
    
    i1 = lines[0]
    i2 = lines[1]

    for i in range(len(i1)):
        i1[i] = [i1[i][0], int(i1[i][1:])]
    for i in range(len(i2)):
        i2[i] = [i2[i][0], int(i2[i][1:])]

    print(i1)
    print(i2)

    wire1 = dict()
    wire2 = dict()
    
    cur = (0,0)
    for i in range(len(i1)):
        curI = i1[i]
        if curI[0] == "R":
            for j in range(curI[1]):
                cur = (cur[0] + 1, cur[1])
                if cur[0] in wire1:
                    wire1[cur[0]].add(cur[1])
                else:
                    wire1[cur[0]] = {cur[1]}
        elif curI[0] == "L":
            for j in range(curI[1]):
                cur = (cur[0] - 1, cur[1])
                if cur[0] in wire1:
                    wire1[cur[0]].add(cur[1])
                else:
                    wire1[cur[0]] = {cur[1]}
        elif curI[0] == "U":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] + 1)
                if cur[0] in wire1:
                    wire1[cur[0]].add(cur[1])
                else:
                    wire1[cur[0]] = {cur[1]}
        elif curI[0] == "D":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] - 1)
                if cur[0] in wire1:
                    wire1[cur[0]].add(cur[1])
                else:
                    wire1[cur[0]] = {cur[1]}
        else:
            print("error")
            break

    cur = (0,0)
    for i in range(len(i2)):
        curI = i2[i]
        if curI[0] == "R":
            for j in range(curI[1]):
                cur = (cur[0] + 1, cur[1])
                if cur[0] in wire2:
                    wire2[cur[0]].add(cur[1])
                else:
                    wire2[cur[0]] = {cur[1]}
        elif curI[0] == "L":
            for j in range(curI[1]):
                cur = (cur[0] - 1, cur[1])
                if cur[0] in wire2:
                    wire2[cur[0]].add(cur[1])
                else:
                    wire2[cur[0]] = {cur[1]}
        elif curI[0] == "U":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] + 1)
                if cur[0] in wire2:
                    wire2[cur[0]].add(cur[1])
                else:
                    wire2[cur[0]] = {cur[1]}
        elif curI[0] == "D":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] - 1)
                if cur[0] in wire2:
                    wire2[cur[0]].add(cur[1])
                else:
                    wire2[cur[0]] = {cur[1]}
        else:
            print("error")
            break

    inter = []
    for x in wire1:
        if x in wire2:
            for y in wire1[x]:
                if y in wire2[x]:
                    inter.append((x,y))

    distances = set()
    for x in inter:
        dist = abs(x[0]) + abs(x[1])
        distances.add(dist)
    
    print(f"Part 1: {min(distances)}")

    interDists = dict()
    for x in inter:
        interDists[x] = [0,0]

    count1 = 0
    cur = (0,0)
    for i in range(len(i1)):
        curI = i1[i]
        if curI[0] == "R":
            for j in range(curI[1]):
                cur = (cur[0] + 1, cur[1])
                count1 += 1
                if cur in interDists:
                    if interDists[cur][0] == 0:
                        interDists[cur][0] = count1
        elif curI[0] == "L":
            for j in range(curI[1]):
                cur = (cur[0] - 1, cur[1])
                count1 += 1
                if cur in interDists:
                    if interDists[cur][0] == 0:
                        interDists[cur][0] = count1
        elif curI[0] == "U":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] + 1)
                count1 += 1
                if cur in interDists:
                    if interDists[cur][0] == 0:
                        interDists[cur][0] = count1
        elif curI[0] == "D":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] - 1)
                count1 += 1
                if cur in interDists:
                    if interDists[cur][0] == 0:
                        interDists[cur][0] = count1
        else:
            print("error")
            break

    count2 = 0
    cur = (0,0)
    for i in range(len(i2)):
        curI = i2[i]
        if curI[0] == "R":
            for j in range(curI[1]):
                cur = (cur[0] + 1, cur[1])
                count2 += 1
                if cur in interDists:
                    if interDists[cur][1] == 0:
                        interDists[cur][1] = count2
        elif curI[0] == "L":
            for j in range(curI[1]):
                cur = (cur[0] - 1, cur[1])
                count2 += 1
                if cur in interDists:
                    if interDists[cur][1] == 0:
                        interDists[cur][1] = count2
        elif curI[0] == "U":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] + 1)
                count2 += 1
                if cur in interDists:
                    if interDists[cur][1] == 0:
                        interDists[cur][1] = count2
        elif curI[0] == "D":
            for j in range(curI[1]):
                cur = (cur[0], cur[1] - 1)
                count2 += 1
                if cur in interDists:
                    if interDists[cur][1] == 0:
                        interDists[cur][1] = count2
        else:
            print("error")
            break

    print(interDists)
    
    iDists = set()
    for x in interDists:
        interDists[x] = interDists[x][0] + interDists[x][1]
        iDists.add(interDists[x])

    print(iDists)

    print(f"Part 2: {min(iDists)}")
    return
