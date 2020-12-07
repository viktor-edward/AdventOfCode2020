import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line))
    f.close()
    return data


def createTree(data):
    tree = {}
    for row in data:
        rowCleaned = row.replace("bags", "bag").replace(",", "").replace(".", "").replace("contain", "")\
            .replace("\n", "").replace("bag", "").split()
        bagName = rowCleaned[0] + rowCleaned[1]
        bagsInBag = []
        bagsInBagCount = math.floor((len(rowCleaned)-2)/3)
        for i in range(0, bagsInBagCount):
            bagsInBag.append((rowCleaned[3*(i+1)] + rowCleaned[3*(i+1) + 1],
                             rowCleaned[3*(i+1)-1]))
        tree[bagName] = bagsInBag
    return tree


def checkGivenBagForGivenColor(tree, color, colorToFind):
    foundStatus = False
    for bagInBag in tree[color]:
        bagColor, amount = bagInBag
        if bagColor == colorToFind:
            foundStatus = True
        else:
            foundStatus = foundStatus or checkGivenBagForGivenColor(tree, bagColor, colorToFind)
    return 1 if foundStatus else 0


def checkAmountOfBagsForGivenColor(tree, color):
    amountOfBags = 0
    if (len(tree[color])) == 0:
        return 1
    else:
        for bagInBag in tree[color]:
            bagColor, amount = bagInBag
            amountOfBags += int(amount)*checkAmountOfBagsForGivenColor(tree, bagColor)
    return amountOfBags + 1


def main():
    data = readFile("../resources/day7_input.txt")
    #data = readFile("../resources/test.txt")

    print("Part one: ")
    tree = createTree(data)
    amountOfGivenColor = 0
    for bagColor in tree:
        amountOfGivenColor += checkGivenBagForGivenColor(tree, bagColor, "shinygold")
    print(amountOfGivenColor)

    print("Part two: ")
    print(checkAmountOfBagsForGivenColor(tree, "shinygold") - 1)


if __name__ == '__main__':
    main()
