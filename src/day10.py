import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(int(line))
    f.close()
    return data


def recDifferentPathsShitperformance(data, startPoint):
    okPaths = 0
    for i in range(1, 4):
        if data[startPoint+i-1] == data[-1]:
            return 1
        elif data[startPoint + i] - data[startPoint] <= 3:
            okPaths += recDifferentPathsShitperformance(data, startPoint + i)
        else:
            break
    return okPaths


def main():
    data = readFile("../resources/day10_input.txt")
    #data = readFile("../resources/test.txt")

    print("Part one: ")
    data.append(0)
    data.sort()
    data.append(data[-1]+3)
    
    diffData = []
    for i in range(len(data)-1):
        diffData.append(data[i+1] - data[i])
    print(diffData.count(1) * diffData.count(3))

    print("Part two: ")
    #print(recDifferentPathsShitperformance(data, 0))
    data.sort(reverse=True)
    possiblePaths = [0, 1]
    for i in range(2, len(data)):
        okSteps = 0
        for j in range(1, 4):
            if i-j == 0:
                break
            elif data[i-j] - data[i] <= 3:
                okSteps += possiblePaths[i-j]
        possiblePaths.append(okSteps)
    print(possiblePaths[-1])


if __name__ == '__main__':
    main()
