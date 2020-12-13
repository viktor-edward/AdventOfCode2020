import math
from functools import reduce


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line).replace("\n", ""))
    f.close()
    return data


def nextBus(time, bus):
    return (math.floor(time / bus) + 1)*bus - time


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def part2Validation(time, busIds):
    for busTuple in busIds:
        bus, offset = busTuple
        test = time % bus
        if not (bus - time % bus) % bus == offset:
            return False
    return True


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def main():
    data = readFile("../resources/day13_input.txt")
    #data = readFile("../resources/test.txt")

    print("Part one: ")
    timeToDepart = int(data[0])
    busIds = []
    for bus in data[1].split(","):
        if bus != "x":
            busIds.append(int(bus))
    print(busIds)
    print(timeToDepart)
    timeTonextBus = []
    for bus in busIds:
        timeTonextBus.append(nextBus(timeToDepart, bus))
    print(timeTonextBus)
    print()

    print("Part two: ")
    busIds = []
    delays = []
    delay = 0
    for bus in data[1].split(","):
        if bus != "x":
            busIds.append(int(bus))
            delays.append(int(bus) - int(delay))
        delay += 1
    print(busIds)
    print(chinese_remainder(busIds, delays))

    '''
    # 67 + 0 = 59 + 2. Find integer solutions and test on the rest of the set
    for i in range(1, 1000000):
        if (59 * i - 2) % 67 == 0:
            passedTest = part2Validation(59 * i - 2, busIds)
            if passedTest:
                print(59 * i - 2)
                break

    # 379y + 41 = 557x + 72. Find integer solutions and test on the rest of the set
    for i in range(1, 100000000000):
        if (557 * i - 31) % 379 == 0:
            passedTest = part2Validation(557*i - 72, busIds)
            if passedTest:
                print(557*i - 72)
                break
    '''


if __name__ == '__main__':
    main()
