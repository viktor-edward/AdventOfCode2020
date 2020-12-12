import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line).replace("\n", "").replace("L", "#"))
    f.close()
    return data


def findSteadyState(data):
    rows = len(data)
    cols = len(data[0])
    changedState = True
    while changedState:
        changedState = False
        newState = []
        for row in range(rows):
            newRow = []
            for col in range(cols):
                if data[row][col] == ".":
                    newRow.append(".")
                elif data[row][col] == "L":
                    if nearbyOccupiedPoints(data, col, row) > 0:
                        newRow.append("L")
                    else:
                        newRow.append("#")
                        changedState = True
                elif data[row][col] == "#":
                    if nearbyOccupiedPoints(data, col, row) < 4:
                        newRow.append("#")
                    else:
                        newRow.append("L")
                        changedState = True
            newState.append(newRow)
        data = newState.copy()
    return newState


def findSteadyStatePart2(data):
    rows = len(data)
    cols = len(data[0])
    changedState = True
    while changedState:
        changedState = False
        newState = []
        for row in range(rows):
            newRow = []
            for col in range(cols):
                if data[row][col] == ".":
                    newRow.append(".")
                elif data[row][col] == "L":
                    if watchableOccupiedPoints(data, col, row) > 0:
                        newRow.append("L")
                    else:
                        newRow.append("#")
                        changedState = True
                elif data[row][col] == "#":
                    if watchableOccupiedPoints(data, col, row) < 5:
                        newRow.append("#")
                    else:
                        newRow.append("L")
                        changedState = True
            newState.append(newRow)
        data = newState.copy()
        #printMatrix(data)
        #print()
    return newState


def nearbyOccupiedPoints(data, col, row):
    nearbyPointsLocal = []
    rows = len(data)-1
    cols = len(data[0])-1
    firstRow, lastRow, firstCol, lastCol = False, False, False, False

    if row == 0:
        firstRow = True
    if row == rows:
        lastRow = True
    if col == 0:
        firstCol = True
    if col == cols:
        lastCol = True

    # Row above
    if not firstRow:
        if not firstCol:
            nearbyPointsLocal.append(data[row-1][col-1])
        if not lastCol:
            nearbyPointsLocal.append(data[row-1][col+1])
        nearbyPointsLocal.append(data[row-1][col])

    # Same row
    if not firstCol:
        nearbyPointsLocal.append(data[row][col - 1])
    if not lastCol:
        nearbyPointsLocal.append(data[row][col + 1])

    # Row below
    if not lastRow:
        if not firstCol:
            nearbyPointsLocal.append(data[row+1][col-1])
        if not lastCol:
            nearbyPointsLocal.append(data[row+1][col+1])
        nearbyPointsLocal.append(data[row+1][col])

    return nearbyPointsLocal.count("#")


def watchableOccupiedPoints(data, col, row):
    watchablePointsLocal = 0
    rows = len(data)-1
    cols = len(data[0])-1

    watchablePointsLocal += checkDirectionForPerson(data, col, row, -1, -1)
    watchablePointsLocal += checkDirectionForPerson(data, col, row, +0, -1)
    watchablePointsLocal += checkDirectionForPerson(data, col, row, +1, -1)
    watchablePointsLocal += checkDirectionForPerson(data, col, row, -1, 0)
    watchablePointsLocal += checkDirectionForPerson(data, col, row, +1, 0)
    watchablePointsLocal += checkDirectionForPerson(data, col, row, -1, +1)
    watchablePointsLocal += checkDirectionForPerson(data, col, row, +0, +1)
    watchablePointsLocal += checkDirectionForPerson(data, col, row, +1, +1)

    return watchablePointsLocal


def checkDirectionForPerson(data, startX, startY, dirX, dirY):
    rows = len(data)-1
    cols = len(data[0])-1
    x = startX + dirX
    y = startY + dirY
    seatFound = 0
    while 0 <= x <= cols and 0 <= y <= rows and not seatFound:
        if data[y][x] == "#":
            seatFound = 1
        elif data[y][x] == "L":
            break
        else:
            x += dirX
            y += dirY
    return seatFound


def printMatrix(data):
    for row in data:
        print(row)


def main():
    data = readFile("../resources/day11_input.txt")
    #data = readFile("../resources/test.txt")
    data2 = data.copy()

    print("Part one: ")
    print(data)

    steadyState = findSteadyState(data)
    numOccupied = 0
    for row in steadyState:
        numOccupied += row.count("#")
    print(steadyState)
    print(numOccupied)

    print("Part two: ")
    steadyState2 = findSteadyStatePart2(data2)
    numOccupied = 0
    for row in steadyState2:
        numOccupied += row.count("#")
    print(steadyState2)
    print(numOccupied)


if __name__ == '__main__':
    main()
