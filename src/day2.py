import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line))
    f.close()
    return data


def numberOfCorrectPasswords(data):
    countCorrectPw = 0
    for row in data:
        minNum, maxNum, letter, pw = splitString(row)
        lettersInPW = countLetters(letter, pw)
        if (lettersInPW >= minNum) and (lettersInPW <= maxNum):
            countCorrectPw += 1
    return countCorrectPw


def numberOfCorrectPasswordsPartTwo(data):
    countCorrectPw = 0
    for row in data:
        num1, num2, letter, pw = splitString(row)
        if (pw[num1-1] == letter) != (pw[num2-1] == letter):
            countCorrectPw += 1
    return countCorrectPw


def splitString(row):
    rowSplit = row.split()
    numbers = rowSplit[0].split("-")
    return int(numbers[0]), int(numbers[1]), rowSplit[1][0], rowSplit[2]


def countLetters(letter, pw):
    count = 0
    for i in range(len(pw)):
        if pw[i] == letter:
            count += 1
    return count


def func2(data):
    
    return 0


def main():
    data = readFile("../resources/day2_input.txt")

    print("Part one: ")
    print(numberOfCorrectPasswords(data))
    

    print("Part two: ")
    print(numberOfCorrectPasswordsPartTwo(data))


if __name__ == '__main__':
    main()
