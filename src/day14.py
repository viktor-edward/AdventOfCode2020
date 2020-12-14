import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line).replace("\n", "").replace(" ", "").replace("mem[", "").replace("]", "").split("="))
    f.close()
    return data


def applyMask(mask, binNum):
    binNumList = list(binNum)
    for i in range(0, len(mask)):
        if mask[i] != "X":
            binNumList[i] = mask[i]
    return ".".join(binNumList).replace(".", "")


def applyMaskPart2(mask, mem):
    binMemList = list(mem)
    binMemArray = [binMemList]
    for i in range(0, len(mask)):
        tempBinMemArray = []
        for arr in binMemArray:
            if mask[i] == "1":
                arr[i] = "1"
                tempBinMemArray.append(arr)
            elif mask[i] == "X":
                tempMemList = arr.copy()
                tempMemList2 = arr.copy()
                tempMemList[i] = "0"
                tempMemList2[i] = "1"
                tempBinMemArray.append(tempMemList)
                tempBinMemArray.append(tempMemList2)
            else:
                tempBinMemArray.append(arr)
        binMemArray = tempBinMemArray.copy()
    for i in range(len(binMemArray)):
        binMemArray[i] = ".".join(binMemArray[i]).replace(".", "")
    return binMemArray


def main():
    data = readFile("../resources/day14_input.txt")
    #data = readFile("../resources/test.txt")

    print("Part one: ")
    memory = dict()
    currentMask = ""
    rowNum = 0
    for row in data:
        rowNum += 1
        if row[0] == "mask":
            currentMask = row[1]
        else:
            binNum = "{:36b}".format(int(row[1])).replace(" ", "0")
            memory[row[0]] = applyMask(currentMask, binNum)

    sumPart1 = 0
    for key, value in memory.items():
        sumPart1 += int(value, 2)
    print(sumPart1)

    print("Part two: ")
    memory = dict()
    currentMask = ""
    rowNum = 0
    for row in data:
        rowNum += 1
        if row[0] == "mask":
            currentMask = row[1]
        else:
            memRead = "{:36b}".format(int(row[0])).replace(" ", "0")
            binMemArray = applyMaskPart2(currentMask, memRead)
            for mem in binMemArray:
                memory[mem] = row[1]

    sumPart2 = 0
    for key, value in memory.items():
        sumPart2 += int(value)
    print(sumPart2)


if __name__ == '__main__':
    main()
