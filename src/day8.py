import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        splitRow = line.split()
        data.append((splitRow[0], splitRow[1]))
    f.close()
    return data


def calculateFinalAccumulator(data):
    accumlator = 0
    i = 0
    visitedRows = set()
    while i not in visitedRows and i < len(data):
        visitedRows.add(i)
        inst, numb = data[i]
        if inst == 'acc':
            accumlator += int(numb)
            i += 1
        elif inst == 'jmp':
            if int(numb) == 0:
                i += 1
            else:
                i += int(numb)
        else:
            i += 1
    if i == len(data):
        return accumlator, True
    else:
        return accumlator, False


def rowsContainingInstr(data, instr):
    rowNumbers = []
    for i in range(0,len(data)-1):
        inst, numb = data[i]
        if inst == instr:
            rowNumbers.append(i)
    return rowNumbers


def main():
    data = readFile("../resources/day8_input.txt")
    #data = readFile("../resources/test.txt")

    print("Part one: ")
    print(calculateFinalAccumulator(data))

    print("Part two: ")
    # Brute force by changing all NOP and JMP
    nopRows = rowsContainingInstr(data, "nop")
    jmpRows = rowsContainingInstr(data, "jmp")
    for row in nopRows:
        tempdata = data.copy()
        inst, numb = data[row]
        tempdata[row] = ("jmp", numb)
        accumulator, statusSucces = calculateFinalAccumulator(tempdata)
        if statusSucces:
            print(accumulator)
    for row in jmpRows:
        tempdata = data.copy()
        inst, numb = data[row]
        tempdata[row] = ("nop", numb)
        accumulator, statusSucces = calculateFinalAccumulator(tempdata)
        if statusSucces:
            print(accumulator)


if __name__ == '__main__':
    main()
