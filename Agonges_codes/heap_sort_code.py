import math

origin = [30, 20, 80, 40, 50, 10, 60, 70, 90]
total = len(origin) - 1

def heap_adjust(line, index, array:list):
    while 2 * index <= line:
        lchile_index = 2 * index
        max_child_index = lchile_index

        if line > lchile_index and array[lchile_index + 1] > array[lchile_index]:
            max_child_index = lchile_index + 1

        if array[max_child_index] > array[index]:
            array[index], array[max_child_index] = array[max_child_index], array[index]
            index = max_child_index
        else:
            break

def max_heap(total, array:list):
    for index in range(total//2, 0, -1):
        heap_adjust(total, index, array)
    return array

def sorts(total, array:list):
    while total > 1:
        array[1], array[total] = array[total], array[1]
        total -= 1
        if total == 2 and array[total] >= array[total-1]:
            break
        heap_adjust(total, 1, array)
    return array

if __name__ == '__main__':
    print(sorts(total, origin))
