import math
import re


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line))
    f.close()
    return data


def checkPasswords(data):
    amountOfCorrectPasswords = 0
    requiredData = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    for row in data:
        if row == "\n":
            if len(requiredData) == 0:
                amountOfCorrectPasswords += 1
            requiredData = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        else:
            for field in row.split():
                if checkValidField(field.split(":")[0], field.split(":")[1]):
                    requiredData.discard(field.split(":")[0])

    if len(requiredData) == 0:
        amountOfCorrectPasswords += 1
    return amountOfCorrectPasswords


def checkValidField(field, value):
    if field == "byr":
        if 1920 <= int(value) <= 2002:
            return True
    elif field == "iyr":
        if 2010 <= int(value) <= 2020:
            return True
    elif field == "eyr":
        if 2020 <= int(value) <= 2030:
            return True
    elif field == "hgt":
        try:
            if value[-1] == 'm' and 150 <= int(value[0:3]) <= 193:
                return True
            elif value[-1] == 'n' and 59 <= int(value[0:2]) <= 76:
                return True
        except:
            print("Height formatting wrong")
    elif field == "hcl":
        if bool(re.match("#[a-z0-9]{6}$", value)):
            return True
    elif field == "ecl":
        if str(value) in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            return True
    elif field == "pid":
        if bool(re.match("[0-9]{9}$", value)):
            return True

    return False


def main():
    data = readFile("../resources/day4_input.txt")

    print(checkPasswords(data))

    '''
    print(checkValidField("byr", "1980"))
    print(checkValidField("iyr", "2012"))
    print(checkValidField("hgt", "74in"))
    print(checkValidField("eyr", "2030"))
    print(checkValidField("ecl", "grn"))
    print(checkValidField("pid", "087499704"))
    print(checkValidField("hcl", "#623a2f"))
    '''

if __name__ == '__main__':
    main()
