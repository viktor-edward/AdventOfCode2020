import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        if line != '\n':
            data.append(str(line).replace("\n", ""))
    f.close()
    return data


def isOkNumber(okValues, numb):
    for key in okValues:
        intervals = okValues[key]
        for intv in intervals:
            valueLower, valueHigher = intv.split("-")
            if int(valueLower) <= int(numb) <= int(valueHigher):
                return True
    return False


def checkOkColumns(numCol, okTickets, okValues):
    okCols = []
    for i in range(2):
        for ticket in okTickets:
            ticketi = int(ticket.split(",")[i])
            print(ticketi)
            foundOkCol = False
            for intv in okValues:
                valueLower, valueHigher = intv.split("-")
                if int(valueLower) <= ticketi <= int(valueHigher):
                    foundOkCol = True
            if not foundOkCol:
                break
        if foundOkCol:
            okCols.append(str(i))
    return okCols


def main():
    data = readFile("../resources/day16_input.txt")
    #data = readFile("../resources/test.txt")


    print("Part one: ")
    okValues = dict()
    notOkValues = []
    print(data)
    parseOkValues = True
    parseNearbyValues = False
    for row in data:
        if row == 'your ticket:':
            parseOkValues = False
        elif row == 'nearby tickets:':
            parseNearbyValues = True
        elif parseOkValues:
            rowTemp = row.replace(" or ", ":").replace(" ", "").split(":")
            tempArray = []
            for i in range(1, len(rowTemp)):
                tempArray.append(rowTemp[i])
            okValues[rowTemp[0]] = tempArray.copy()
        elif parseNearbyValues:
            tempRow = row.split(",")
            for numb in tempRow:
                if not isOkNumber(okValues, numb):
                    notOkValues.append(int(numb))
    print(notOkValues)
    print(sum(notOkValues))


    print("Part two: ")
    okValues = dict()
    okTickets = []
    print(data)
    parseOkValues = True
    parseNearbyValues = False
    for row in data:
        if row == 'your ticket:':
            parseOkValues = False
        elif row == 'nearby tickets:':
            parseNearbyValues = True
        elif parseOkValues:
            rowTemp = row.replace(" or ", ":").replace(" ", "").split(":")
            tempArray = []
            for i in range(1, len(rowTemp)):
                tempArray.append(rowTemp[i])
            okValues[rowTemp[0]] = tempArray.copy()
        elif parseNearbyValues:
            tempRow = row.split(",")
            okTicketLocal = True
            for numb in tempRow:
                if not isOkNumber(okValues, numb):
                    okTicketLocal = False
            if okTicketLocal:
                okTickets.append(row)


    myTicket = [109,101,79,127,71,59,67,61,173,157,163,103,83,97,73,167,53,107,89,131]
    numCol = len(myTicket)

    print(okValues)

    print("departurelocation")
    print(checkOkColumns(numCol, okTickets, okValues["departurelocation"]))
    '''print("departurestation")
    print(checkOkColumns(numCol, okTickets, okValues["departurestation"]))
    print("departureplatform")
    print(checkOkColumns(numCol, okTickets, okValues["departureplatform"]))
    print("departuretrack")
    print(checkOkColumns(numCol, okTickets, okValues["departuretrack"]))
    print("departuredate")
    print(checkOkColumns(numCol, okTickets, okValues["departuredate"]))
    print("departuredate")
    print(checkOkColumns(numCol, okTickets, okValues["departuredate"]))'''






if __name__ == '__main__':
    main()
