import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line).replace("\n", ""))
    f.close()
    return data


def rotatePoints(wpx, wpy, inst, instNum):
    if (inst == "R" and instNum == 90) or (inst == "L" and instNum == 270):
        return wpy, -wpx
    elif (inst == "R" and instNum == 270) or (inst == "L" and instNum == 90):
        return -wpy, wpx
    elif (inst == "R" and instNum == 180) or (inst == "L" and instNum == 180):
        return -wpx, -wpy
    else:
        print("Error!")
        return 0, 0


def main():
    data = readFile("../resources/day12_input.txt")
    #data = readFile("../resources/test.txt")

    print("Part one: ")
    dirD, x, y = 0, 0, 0
    dirV = ["E", "S", "W", "N"]
    for row in data:
        inst = row[0]
        instNum = int(row[1:])

        if inst == "R":
            dirD = int((dirD + instNum / 90) % 4)
        elif inst == "L":
            dirD = int((dirD - instNum / 90) % 4)
        else:
            if inst == "F":
                inst = dirV[dirD]
            if inst == "E":
                x += instNum
            elif inst == "S":
                y -= instNum
            elif inst == "W":
                x -= instNum
            elif inst == "N":
                y += instNum

    answer = abs(x) + abs(y)
    print(answer)
    print(x)
    print(y)

    print("Part two: ")
    x, y, wpx, wpy = 0, 0, 10, 1
    for row in data:
        inst = row[0]
        instNum = int(row[1:])
        if inst == "R" or inst == "L":
            wpx, wpy = rotatePoints(wpx, wpy, inst, instNum)
        elif inst == "E":
            wpx += instNum
        elif inst == "S":
            wpy -= instNum
        elif inst == "W":
            wpx -= instNum
        elif inst == "N":
            wpy += instNum
        elif inst == "F":
            x += wpx*instNum
            y += wpy*instNum

    answer = abs(x) + abs(y)
    print(answer)
    print(x)
    print(y)


if __name__ == '__main__':
    main()
