import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line))
    f.close()
    return data


def numberOfTress(right, left, data):
    numberOfTrees = 0
    xrepeat = len(data[0])-1
    x = 0
    for i in range(left, len(data), left):
        x = (x+right) % xrepeat
        if data[i][x] == '#':
            numberOfTrees += 1
    return numberOfTrees


def main():
    data = readFile("../resources/day3_input.txt")

    print("Part one: ")
    print(numberOfTress(3, 1, data))

    print("Part two: ")
    n1 = numberOfTress(1, 1, data)
    n2 = numberOfTress(3, 1, data)
    n3 = numberOfTress(5, 1, data)
    n4 = numberOfTress(7, 1, data)
    n5 = numberOfTress(1, 2, data)

    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)
    print(n1*n2*n3*n4*n5)


if __name__ == '__main__':
    main()
