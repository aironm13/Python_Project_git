import random


numlist = [random.randint(1, 100) for _ in range(10)]
print(numlist)

def main():
    lenght = len(numlist)
    for line in range(lenght):
        for row in range(lenght - line - 1):
            if numlist[row] > numlist[row + 1]:
                numlist[row], numlist[row + 1] = numlist[row + 1], numlist[row]
    print(numlist)

if __name__ == '__main__':
    main()