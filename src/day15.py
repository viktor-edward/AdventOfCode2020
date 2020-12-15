import math


def func1(data):
    
    return 0


def func2(data):
    
    return 0


def main():
    data = [2, 15, 0, 9, 1, 20]
    #data = [0, 3, 6] # Test
    spokenWords = dict()
    spokenWords["2"] = 1
    spokenWords["15"] = 2
    spokenWords["0"] = 3
    spokenWords["9"] = 4
    spokenWords["1"] = 5
    lastWord = "20"
    n = 2020

    print("Part one: ")
    for i in range(len(data), n):
        print(lastWord)
        print(i)
        print()
        if lastWord in spokenWords:
            lastWordTemp = str(i - int(spokenWords[lastWord]))
            spokenWords[lastWord] = str(i)
            lastWord = lastWordTemp
        else:
            spokenWords[lastWord] = str(i)
            lastWord = "0"
    print(spokenWords)
    print(lastWord)

    print("Part two: ")
    spokenWords = dict()
    spokenWords["2"] = 1
    spokenWords["15"] = 2
    spokenWords["0"] = 3
    spokenWords["9"] = 4
    spokenWords["1"] = 5
    lastWord = "20"
    n = 30000000
    for i in range(len(data), n):
        if lastWord in spokenWords:
            lastWordTemp = str(i - int(spokenWords[lastWord]))
            spokenWords[lastWord] = str(i)
            lastWord = lastWordTemp
        else:
            spokenWords[lastWord] = str(i)
            lastWord = "0"
    #print(spokenWords)
    print(lastWord)
    


if __name__ == '__main__':
    main()
