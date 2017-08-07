def selection_sort(array):
    for i in range(len(array)):
        smallest_index = i
        for j in range(i + 1, len(array)):
            if array[smallest_index] > array[j]:
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]
    return array


if __name__ == '__main__':
    array = [1, 3, 5, 7, 2, 4, 6, 8]
    print selection_sort(array)
