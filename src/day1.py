import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(float(line))
    f.close()
    return data


def findMultiNumber(data, numberToFind):
    numberOfPoints = len(data)
    for i in range(0,numberOfPoints):
        for j in range(1,numberOfPoints):
            if data[i]+data[j] == numberToFind:
                return data[i], data[j]
    print("Number not found")
    return 0, 0


def findMultiNumberThree(data, numberToFind):
    numberOfPoints = len(data)
    for i in range(0,numberOfPoints):
        for j in range(1,numberOfPoints):
            for k in range(1, numberOfPoints):
                if data[i]+data[j]+data[k] == numberToFind:
                    return data[i], data[j], data[k]
    print("Number not found")
    return 0, 0


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")
    numberToFind = 2020
    n1, n2 = findMultiNumber(data, numberToFind)
    print("Numbers were: " + str(n1) + " and " + str(n2))
    print(str(n1*n2))

    print("Part two: ")
    n1, n2, n3 = findMultiNumberThree(data, numberToFind)
    print("Numbers were: " + str(n1) + " and " + str(n2)+ " and " + str(n3))
    print(str(n1*n2*n3))


if __name__ == '__main__':
    main()
