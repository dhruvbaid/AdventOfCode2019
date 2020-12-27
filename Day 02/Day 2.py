def part1():
    with open("Day 2 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    lines = lines[0].split(",")

    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

    print(lines)

    lines[1] = 12
    lines[2] = 2

    i = 0
    while i < len(lines):
        if lines[i] == 1:
            lines[lines[i+3]] = lines[lines[i+1]] + lines[lines[i+2]]
            i += 4
        elif lines[i] == 2:
            lines[lines[i+3]] = lines[lines[i+1]] * lines[lines[i+2]]
            i += 4
        elif lines[i] == 99:
            break
        else:
            print("error")
            break
    
    return lines[0]

def part2():
    with open("Day 2 Input.txt", mode = 'r') as f:
        lines = f.readlines()

    lines = lines[0].split(",")

    for i in range(len(lines)):
        lines[i] = int(lines[i].strip())

    for a in range(100):
        for b in range(100):
            tmp = []
            for x in lines:
                tmp.append(x)
            tmp[1] = a
            tmp[2] = b

            i = 0
            while i < len(tmp):
                if tmp[i] == 1:
                    tmp[tmp[i+3]] = tmp[tmp[i+1]] + tmp[tmp[i+2]]
                    i += 4
                elif tmp[i] == 2:
                    tmp[tmp[i+3]] = tmp[tmp[i+1]] * tmp[tmp[i+2]]
                    i += 4
                elif tmp[i] == 99:
                    break
                else:
                    print("error")
                    break
            res = tmp[0]
            if res == 19690720:
                return((100 * a) + b)
