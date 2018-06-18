import random


def main():
    numlist = [random.randint(1, 100) for _ in range(10)]
    print(numlist)
    lenght = len(numlist)

    for i in range(1, lenght):
        var = numlist[i]
        position = i

        while position > 0 and numlist[position - 1] > var:
            numlist[position] = numlist[position - 1]
            position -= 1
        numlist[position] = var
    print(numlist)

if __name__ == '__main__':
    main()