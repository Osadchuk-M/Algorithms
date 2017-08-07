def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    array = [1, 3, 5, 7, 9]

    index_of_1 = binary_search(array, 1)
    assert 1 == array[index_of_1]

    must_be_None = binary_search(array, 2)
    assert must_be_None is None
