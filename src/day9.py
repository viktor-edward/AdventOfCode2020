import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(int(line))
    f.close()
    return data


def checkIfContainSum(data, number):
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            if data[i] + data[j] == number:
                return data[i], data[j], number, True
    return 0, 0, number, False


def findContinousSubSetSum(data, number):
    for i in range(len(data)):
        tempSum = data[i]
        for j in range(i+1, len(data)):
            tempSum += data[j]
            if tempSum == number:
                return data[i:j+1], True
            elif tempSum > number:
                break
    return 0, False


def main():
    data = readFile("../resources/day9_input.txt")

    print("Part one: ")
    for i in range(25, len(data)):
        n1, n2, number, status = checkIfContainSum(data[i-25: i], data[i])
        if not status:
            print(number)
            break

    print("Part two: ")
    dataSet, status2 = findContinousSubSetSum(data[0:i], number)
    print(dataSet)
    print(min(dataSet) + max(dataSet))


if __name__ == '__main__':
    main()
