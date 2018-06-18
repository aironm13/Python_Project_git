import random


def main():
    numlist = [random.randint(1, 100) for _ in range(10)]
    length = len(numlist)
    print(numlist)

    for line in range(length):
        temp = line
        for row in range(line + 1, length):
            if numlist[row] < numlist[temp]:
                temp = row
        else:
            numlist[line], numlist[temp] = numlist[temp], numlist[line]
    print(numlist)

if __name__ == '__main__':
    main()