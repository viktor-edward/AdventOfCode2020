import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line))
    f.close()
    return data


def countCounts(data):
    sumCounts = 0
    counts = set()
    for row in data:
        if row == "\n":
            sumCounts += len(counts)
            counts = set()
        else:
            row = row.strip("\n")
            for i in range(0, len(row)):
                counts.add(row[i])
    
    return sumCounts + len(counts)


def countCounts2(data):
    sumCounts = 0
    counts, commonAnswers = set(), set()
    firstRowBlock = 0
    for row in data:
        if row == "\n":
            sumCounts += len(commonAnswers)
            commonAnswers = set()
            firstRowBlock = 0
        else:
            row = row.strip("\n")
            counts = set()
            for i in range(0, len(row)):
                counts.add(row[i])
            if firstRowBlock == 0:
                commonAnswers = counts
                firstRowBlock += 1
            else:
                commonAnswers = commonAnswers & counts

    return sumCounts + len(commonAnswers)


def main():
    data = readFile("../resources/day6_input.txt")

    print("Part one: ")
    print(countCounts(data))

    print("Part two: ")
    print(countCounts2(data))


if __name__ == '__main__':
    main()
