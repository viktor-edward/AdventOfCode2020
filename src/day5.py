import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line))
    f.close()
    return data


def calculateSeatNumber(row):
    rowStr = row[0:7]
    colStr = row[7:10]
    return int(calculateRowNumber(rowStr)*8 + calculateColNumber(colStr))


def calculateRowNumber(rowStr):
    front, back = 0, 127
    for i in range(0, len(rowStr)):
        if rowStr[i] == "F":
            back = (front+back+1)/2 - 1
        elif rowStr[i] == "B":
            front = (front+back+1)/2
    if front == back:
        return front
    else:
        print("Error")
        return 0


def calculateColNumber(rowCol):
    left, right = 0, 7
    for i in range(0, len(rowCol)):
        if rowCol[i] == "L":
            right = (left+right+1)/2 - 1
        elif rowCol[i] == "R":
            left = (left+right+1)/2
    if left == right:
        return left
    else:
        print("Error")
        return 0


def main():
    data = readFile("../resources/day5_input.txt")
    print("Part one: ")
    allSeatNumbers = set()
    for row in data:
        allSeatNumbers.add(calculateSeatNumber(row))
    print(max(allSeatNumbers))

    print("Part two: ")
    maxSeat = 127*8 + 7
    allSeats = set(range(0, maxSeat))
    print(allSeats.difference(allSeatNumbers))


if __name__ == '__main__':
    main()
