def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [item for item in array[1:] if item <= pivot]
    greater = [item for item in array[1:] if item > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    from random import randint

    for i in range(10):
        arr = [randint(1, 100) for _ in range(10)]
        arr = quick_sort(arr)
        test_index = randint(0, len(arr)-2)
        assert arr[test_index] < arr[test_index+1], "arr[%s] >= arr[%s] in %s" % (test_index, test_index+1, arr)
